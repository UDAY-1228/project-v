"""
AI-Yantra - API Routes
=======================
FastAPI router for all AI-Yantra endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService,
    AuthService,
    AIToolService,
    AutomationService,
    ModelControlService,
    AnalyticsService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/ai-yantra", tags=["AI-Yantra"])


@router.get("/dashboard/stats", response_model=APIResponse)
async def get_dashboard_stats():
    try:
        stats = await DashboardService.get_stats()
        return APIResponse(success=True, data=stats, message="Dashboard stats retrieved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/dashboard/activity", response_model=APIResponse)
async def get_dashboard_activity(limit: int = Query(10, ge=1, le=50)):
    try:
        activities = await DashboardService.get_recent_activity(limit)
        return APIResponse(success=True, data=activities, count=len(activities))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/ai-tools", response_model=APIResponse)
async def create_ai_tool(data: AIToolCreate):
    try:
        tool_id = await AIToolService.create_tool(data.model_dump())
        return APIResponse(success=True, data={"id": tool_id}, message="AI Tool created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/ai-tools", response_model=APIResponse)
async def get_ai_tools(category: Optional[str] = None):
    try:
        tools = await AIToolService.get_all_tools(category)
        return APIResponse(success=True, data=tools, count=len(tools))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/ai-tools/{tool_id}", response_model=APIResponse)
async def get_ai_tool(tool_id: str):
    try:
        tool = await AIToolService.get_tool(tool_id)
        if not tool:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=tool)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/ai-tools/{tool_id}", response_model=APIResponse)
async def update_ai_tool(tool_id: str, data: AIToolCreate):
    try:
        updated = await AIToolService.update_tool(tool_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/ai-tools/{tool_id}", response_model=APIResponse)
async def delete_ai_tool(tool_id: str):
    try:
        deleted = await AIToolService.delete_tool(tool_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/ai-tools/{tool_id}/toggle", response_model=APIResponse)
async def toggle_ai_tool(tool_id: str):
    try:
        toggled = await AIToolService.toggle_tool_status(tool_id)
        return APIResponse(success=toggled, message="Status toggled" if toggled else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/automations", response_model=APIResponse)
async def create_automation(data: AutomationCreate):
    try:
        automation_id = await AutomationService.create_automation(data.model_dump())
        return APIResponse(success=True, data={"id": automation_id}, message="Automation created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/automations", response_model=APIResponse)
async def get_automations(is_active: Optional[bool] = None):
    try:
        automations = await AutomationService.get_all_automations(is_active)
        return APIResponse(success=True, data=automations, count=len(automations))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/automations/{automation_id}", response_model=APIResponse)
async def get_automation(automation_id: str):
    try:
        automation = await AutomationService.get_automation(automation_id)
        if not automation:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=automation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/automations/{automation_id}", response_model=APIResponse)
async def update_automation(automation_id: str, data: AutomationCreate):
    try:
        updated = await AutomationService.update_automation(automation_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/automations/{automation_id}", response_model=APIResponse)
async def delete_automation(automation_id: str):
    try:
        deleted = await AutomationService.delete_automation(automation_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/automations/{automation_id}/toggle", response_model=APIResponse)
async def toggle_automation(automation_id: str):
    try:
        toggled = await AutomationService.toggle_automation(automation_id)
        return APIResponse(success=toggled, message="Automation toggled" if toggled else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/automations/{automation_id}/run", response_model=APIResponse)
async def run_automation(automation_id: str):
    try:
        ran = await AutomationService.run_automation(automation_id)
        return APIResponse(success=ran, message="Automation executed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/models", response_model=APIResponse)
async def create_model(data: ModelCreate):
    try:
        model_id = await ModelControlService.create_model(data.model_dump())
        return APIResponse(success=True, data={"id": model_id}, message="Model created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models", response_model=APIResponse)
async def get_models():
    try:
        models = await ModelControlService.get_all_models()
        return APIResponse(success=True, data=models, count=len(models))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models/{model_id}", response_model=APIResponse)
async def get_model(model_id: str):
    try:
        model = await ModelControlService.get_model(model_id)
        if not model:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=model)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/models/{model_id}", response_model=APIResponse)
async def update_model(model_id: str, data: ModelCreate):
    try:
        updated = await ModelControlService.update_model(model_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/models/{model_id}", response_model=APIResponse)
async def delete_model(model_id: str):
    try:
        deleted = await ModelControlService.delete_model(model_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/models/{model_id}/start", response_model=APIResponse)
async def start_model(model_id: str):
    try:
        started = await ModelControlService.start_model(model_id)
        return APIResponse(success=started, message="Model started" if started else "Failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/models/{model_id}/stop", response_model=APIResponse)
async def stop_model(model_id: str):
    try:
        stopped = await ModelControlService.stop_model(model_id)
        return APIResponse(success=stopped, message="Model stopped" if stopped else "Failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/analytics", response_model=APIResponse)
async def get_analytics(metric_type: Optional[str] = None):
    try:
        metrics = await AnalyticsService.get_metrics(metric_type)
        return APIResponse(success=True, data=metrics, count=len(metrics))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analytics", response_model=APIResponse)
async def record_metric(data: dict):
    try:
        metric_id = await AnalyticsService.record_metric(data)
        return APIResponse(success=True, data={"id": metric_id}, message="Metric recorded")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reports", response_model=APIResponse)
async def create_report(data: ReportCreate):
    try:
        report_id = await ReportService.create_report(data.model_dump())
        return APIResponse(success=True, data={"id": report_id}, message="Report created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports", response_model=APIResponse)
async def get_reports(report_type: Optional[str] = None):
    try:
        reports = await ReportService.get_all_reports(report_type)
        return APIResponse(success=True, data=reports, count=len(reports))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/reports/{report_id}", response_model=APIResponse)
async def get_report(report_id: str):
    try:
        report = await ReportService.get_report(report_id)
        if not report:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=report)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/reports/{report_id}", response_model=APIResponse)
async def delete_report(report_id: str):
    try:
        deleted = await ReportService.delete_report(report_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/settings", response_model=APIResponse)
async def get_settings():
    try:
        settings = await SettingsService.get_settings()
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: SettingsCreate):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump())
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/logout", response_model=APIResponse)
async def logout(user_id: str = Query(...)):
    try:
        from .services import AuthService
        logged_out = await AuthService.logout(user_id)
        return APIResponse(success=logged_out, message="Logged out successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
