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

  constructor(private data_service: DataService) {}

  ngOnInit() {
    this.loadMockData();
    this.loadPythonData();
  }
  private loadMockData() {
    this.data_service.getMockApiUrl().subscribe({
      next: (posts) => {
        this.posts = posts;
      },
      error: (error) => {
        this.errorMessage = error;
      },
    });
  }

  private loadPythonData() {
    this.data_service.getPythonApiUrl().subscribe({
      next: (response) => {
        this.message = response;
        console.log(this.message);
      },
      error: (error) => {
        this.errorMessage = error;
      },
    });
  }

}
