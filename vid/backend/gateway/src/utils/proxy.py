"""
VID API Gateway – Route Proxy Utilities
Forwards requests to the appropriate microservice.
"""
import logging
import requests
from flask import g, jsonify, request, Response

logger = logging.getLogger(__name__)


def proxy_request(service_url: str, path: str = "", timeout: int = 10) -> Response:
    """
    Forward the current Flask request to a downstream microservice.
    Injects tenant headers and forwards auth token.
    """
    target_url = f"{service_url.rstrip('/')}/{path.lstrip('/')}"

    # Forward headers
    headers = {
        key: value
        for key, value in request.headers
        if key.lower() not in {"host", "content-length"}
    }

    # Inject tenant context
    if hasattr(g, "institution_id") and g.institution_id:
        headers["X-Institution-ID"] = g.institution_id
    if hasattr(g, "current_user_id") and g.current_user_id:
        headers["X-User-ID"] = g.current_user_id
    if hasattr(g, "user_type") and g.user_type:
        headers["X-User-Type"] = g.user_type

    try:
        resp = requests.request(
            method=request.method,
            url=target_url,
            headers=headers,
            params=request.args,
            json=request.get_json(silent=True),
            data=request.form or None,
            files=request.files or None,
            timeout=timeout,
            allow_redirects=False,
        )
        return Response(
            response=resp.content,
            status=resp.status_code,
            headers=dict(resp.headers),
            content_type=resp.headers.get("Content-Type", "application/json"),
        )
    except requests.exceptions.ConnectionError:
        logger.error(f"Service unavailable: {target_url}")
        return jsonify({"error": "Service Unavailable", "service": service_url}), 503
    except requests.exceptions.Timeout:
        logger.error(f"Service timeout: {target_url}")
        return jsonify({"error": "Gateway Timeout"}), 504
    except Exception as exc:
        logger.exception(f"Proxy error: {exc}")
        return jsonify({"error": "Bad Gateway"}), 502
