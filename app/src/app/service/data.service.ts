import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

interface Post {
  userId: number;
  id: number;
  title: string;
  body: string;
}

@Injectable({
  providedIn: 'root',
})
export class DataService {
  mockApiUrl: string = 'https://jsonplaceholder.typicode.com/posts';
  pythonApiUrlInto: string = 'http://127.0.0.1:5000/api/intro';
  pythonApiUrlTasks: string = 'http://127.0.0.1:5000/api/tasks';

  constructor(private http: HttpClient) {}

  getMockApiUrl(): Observable<Post[]> {
    return this.http.get<Post[]>(this.mockApiUrl);
  }

  getPythonApiUrlIntro(): Observable<Post[]> {
    return this.http.get<Post[]>(this.pythonApiUrlInto);
  }

  getPythonApiUrlTasks(): Observable<any[]> {
    return this.http.get<any[]>(this.pythonApiUrlTasks);
  }
}
