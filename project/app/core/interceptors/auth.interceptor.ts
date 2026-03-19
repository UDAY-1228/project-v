import { HttpInterceptorFn, HttpRequest, HttpHandlerFn, HttpErrorResponse } from '@angular/common/http';
import { inject } from '@angular/core';
import { Router } from '@angular/router';
import { catchError, throwError } from 'rxjs';
import { Store } from '@ngxs/store';
import { AuthState } from '../state/auth.state';
import { Logout } from '../state/auth.actions';

export const authInterceptor: HttpInterceptorFn = (req: HttpRequest<unknown>, next: HttpHandlerFn) => {
  const store = inject(Store);
  const router = inject(Router);
  const token = store.selectSnapshot(AuthState.token);

  let authReq = req;
  if (token) {
    authReq = req.clone({
      setHeaders: { Authorization: `Bearer ${token}` },
    });
  }

  return next(authReq).pipe(
    catchError((error: HttpErrorResponse) => {
      if (error.status === 401) {
        store.dispatch(new Logout());
        router.navigate(['/login']);
      }
      return throwError(() => error);
    })
  );
};
