import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ProfileService } from './profile.service';
import { Profile } from './profile.model';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  profileForm!: FormGroup; 
  editing = false;
  selectedFile: File | null = null; //variable para la foto a

  constructor(private fb: FormBuilder, private profileService: ProfileService) { }

  ngOnInit(): void {
    this.profileForm = this.fb.group({
      username: [{ value: '', disabled: true }, Validators.required],
      first_name: [{ value: '', disabled: true }, Validators.required],
      last_name: [{ value: '', disabled: true }, Validators.required],
      email: [{ value: '', disabled: true }, [Validators.required, Validators.email]],
    });

    this.loadUserProfile();
  }

  loadUserProfile(): void {
    this.profileService.getProfile().subscribe(
      (profile: Profile) => {
        this.profileForm.patchValue(profile);
      },
      error => {
        console.error('Error al cargar el perfil', error);
      }
    );
  }

  toggleEditing() {
    this.editing = !this.editing;
    if (this.editing) {
      this.profileForm.enable();
    } else {
      this.profileForm.disable();
    }
  }

  saveProfile() {
    if (this.profileForm.valid) {
      const updatedProfile: Profile = this.profileForm.value;
      this.profileService.updateProfile(updatedProfile).subscribe(
        response => {
          console.log('Perfil actualizado', response);
          this.editing = false;
          this.profileForm.disable();
        },
        error => {
          console.error('Error al actualizar el perfil', error);
        }
      );
    }
  }
}