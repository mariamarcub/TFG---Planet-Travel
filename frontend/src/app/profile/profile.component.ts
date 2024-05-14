import { Component, Input, OnInit  } from '@angular/core';
import { ProfileService } from './profile.service';
import { Profile } from './profile.model';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit{
  profile: Profile[] = [];
  @Input() mostrarBody: boolean = false;

  constructor(private ProfileService: ProfileService) {}

  ngOnInit() {
    this.ProfileService.getProfile().subscribe({
      next: (data) => {
        this.profile = data;
      },
      error: (error) => {
        console.error('There was an error!', error);
      }
    });
  }
}

