import {Component, OnInit} from '@angular/core';
import { CommonModule } from '@angular/common';
import { DataService } from './service/data.service';

interface Post {
  userId: number;
  id: number;
  title: string;
  body: string;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  posts: Post[] = [];
  errorMessage!: string;
  message: any = '';
  task: any = '';

  constructor(private data_service: DataService) {}

  onGetPythonApiUrlIntro() {
    this.data_service.getPythonApiUrlIntro().subscribe({
      next: (response) => {
        this.message = response;
        console.log(this.message);
      },
      error: (error) => {
        this.errorMessage = error;
      },
    });
  }

  onGetPythonApiUrlTasks() {
    this.data_service.getPythonApiUrlTasks().subscribe({
      next: (response) => {
        this.task = response;
        console.log(this.task);
      },
      error: (error) => {
        this.errorMessage = error;
      },
    });
  }

  onGetMockApiUrl() {
    this.data_service.getMockApiUrl().subscribe({
      next: (posts) => {
        this.posts = posts;
      },
      error: (error) => {
        this.errorMessage = error;
      },
    });
  }

}
