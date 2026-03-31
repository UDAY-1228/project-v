"""
Transport Coordinator - API Routes
==================================
FastAPI router for all Transport Coordinator endpoints.
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from .models import *
from .services import (
    DashboardService,
    VehicleService,
    RouteService,
    StudentTransportService,
    TripLogService,
    ReportService,
    SettingsService,
)

router = APIRouter(prefix="/transport-coordinator", tags=["Transport Coordinator"])


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


@router.post("/vehicles", response_model=APIResponse)
async def create_vehicle(data: VehicleCreate):
    try:
        vehicle_id = await VehicleService.create_vehicle(data.model_dump())
        return APIResponse(success=True, data={"id": vehicle_id}, message="Vehicle created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/vehicles", response_model=APIResponse)
async def get_vehicles(status: Optional[str] = None):
    try:
        vehicles = await VehicleService.get_all_vehicles(status)
        return APIResponse(success=True, data=vehicles, count=len(vehicles))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/vehicles/{vehicle_id}", response_model=APIResponse)
async def get_vehicle(vehicle_id: str):
    try:
        vehicle = await VehicleService.get_vehicle(vehicle_id)
        if not vehicle:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=vehicle)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/vehicles/{vehicle_id}", response_model=APIResponse)
async def update_vehicle(vehicle_id: str, data: VehicleCreate):
    try:
        updated = await VehicleService.update_vehicle(vehicle_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/vehicles/{vehicle_id}", response_model=APIResponse)
async def delete_vehicle(vehicle_id: str):
    try:
        deleted = await VehicleService.delete_vehicle(vehicle_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/routes", response_model=APIResponse)
async def create_route(data: RouteCreate):
    try:
        route_id = await RouteService.create_route(data.model_dump())
        return APIResponse(success=True, data={"id": route_id}, message="Route created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/routes", response_model=APIResponse)
async def get_routes(status: Optional[str] = None):
    try:
        routes = await RouteService.get_all_routes(status)
        return APIResponse(success=True, data=routes, count=len(routes))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/routes/{route_id}", response_model=APIResponse)
async def get_route(route_id: str):
    try:
        route = await RouteService.get_route(route_id)
        if not route:
            return APIResponse(success=False, error="Not Found")
        return APIResponse(success=True, data=route)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/routes/{route_id}", response_model=APIResponse)
async def update_route(route_id: str, data: RouteCreate):
    try:
        updated = await RouteService.update_route(route_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/routes/{route_id}", response_model=APIResponse)
async def delete_route(route_id: str):
    try:
        deleted = await RouteService.delete_route(route_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/student-transports", response_model=APIResponse)
async def create_student_transport(data: StudentTransportCreate):
    try:
        transport_id = await StudentTransportService.create_student_transport(data.model_dump())
        return APIResponse(success=True, data={"id": transport_id}, message="Student transport created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/student-transports", response_model=APIResponse)
async def get_student_transports(route_id: Optional[str] = None, is_active: Optional[bool] = None):
    try:
        transports = await StudentTransportService.get_all_student_transports(route_id, is_active)
        return APIResponse(success=True, data=transports, count=len(transports))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/student-transports/{transport_id}", response_model=APIResponse)
async def update_student_transport(transport_id: str, data: StudentTransportCreate):
    try:
        updated = await StudentTransportService.update_student_transport(transport_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/student-transports/{transport_id}", response_model=APIResponse)
async def delete_student_transport(transport_id: str):
    try:
        deleted = await StudentTransportService.delete_student_transport(transport_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/trip-logs", response_model=APIResponse)
async def create_trip_log(data: TripLogCreate):
    try:
        trip_id = await TripLogService.create_trip_log(data.model_dump())
        return APIResponse(success=True, data={"id": trip_id}, message="Trip log created")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/trip-logs", response_model=APIResponse)
async def get_trip_logs(vehicle_id: Optional[str] = None, route_id: Optional[str] = None):
    try:
        trips = await TripLogService.get_all_trip_logs(vehicle_id, route_id)
        return APIResponse(success=True, data=trips, count=len(trips))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/trip-logs/{trip_id}", response_model=APIResponse)
async def update_trip_log(trip_id: str, data: TripLogCreate):
    try:
        updated = await TripLogService.update_trip_log(trip_id, data.model_dump())
        return APIResponse(success=updated, message="Updated" if updated else "Not modified")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reports", response_model=APIResponse)
async def create_report(data: TransportReportCreate):
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


@router.delete("/reports/{report_id}", response_model=APIResponse)
async def delete_report(report_id: str):
    try:
        deleted = await ReportService.delete_report(report_id)
        return APIResponse(success=deleted, message="Deleted" if deleted else "Not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/settings", response_model=APIResponse)
async def get_settings(institution_id: Optional[str] = None):
    try:
        settings = await SettingsService.get_settings(institution_id)
        return APIResponse(success=True, data=settings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/settings", response_model=APIResponse)
async def update_settings(data: TransportSettingsCreate, institution_id: Optional[str] = None):
    try:
        settings_id = await SettingsService.upsert_settings(data.model_dump(), institution_id)
        return APIResponse(success=True, data={"id": settings_id}, message="Settings saved")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
