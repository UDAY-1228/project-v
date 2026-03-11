import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class ApiService {
    private baseUrl = 'http://localhost:8000/api/v1';

    constructor(private http: HttpClient) { }

    getConfig(): Observable<any> {
        return this.http.get(`${this.baseUrl}/system/config`);
    }

    getAttendance(): Observable<any> {
        return this.http.get(`${this.baseUrl}/attendance/`);
    }

    getCourses(): Observable<any> {
        return this.http.get(`${this.baseUrl}/lms/`);
    }
}
