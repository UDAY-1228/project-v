import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { TokenResponse, LoginRequest, User } from '../../models';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly base = `${environment.apiUrl}/auth`;

  constructor(private http: HttpClient) {}

  login(data: LoginRequest & { institution_code?: string }): Observable<TokenResponse> {
    return this.http.post<TokenResponse>(`${this.base}/login`, data);
  }

  register(data: any): Observable<User> {
    return this.http.post<User>(`${this.base}/register`, data);
  }

  logout(): Observable<any> {
    return this.http.post(`${this.base}/logout`, {});
  }

  forgotPassword(email: string): Observable<any> {
    return this.http.post(`${this.base}/forgot-password`, { email });
  }

  resetPassword(email: string, newPassword: string): Observable<any> {
    return this.http.post(`${this.base}/reset-password`, { email, new_password: newPassword });
  }

  getMe(): Observable<User> {
    return this.http.get<User>(`${this.base}/me`);
  }

  refreshToken(refreshToken: string): Observable<{ access_token: string }> {
    return this.http.post<{ access_token: string }>(`${this.base}/refresh`, { refresh_token: refreshToken });
  }
}
