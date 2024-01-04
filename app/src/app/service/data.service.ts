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
  pythonApiUrl: string = 'http://127.0.0.1:5000/api/intro';

  constructor(private http: HttpClient) {}

  getMockApiUrl(): Observable<Post[]> {
    return this.http.get<Post[]>(this.mockApiUrl);
  }

  getPythonApiUrl(): Observable<Post[]> {
    return this.http.get<Post[]>(this.pythonApiUrl);
  }
}
