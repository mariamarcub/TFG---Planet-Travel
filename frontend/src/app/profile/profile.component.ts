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
  selectedFile: File | null = null; // variable para la foto
  profilePhotoUrl: string | null = null; // URL de la foto de perfil
  savedSuccessfully: boolean = false; //Mensaje creado con exito


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

  //Cargar la url de la foto y los datos del cliente
  loadUserProfile(): void {
    this.profileService.getProfile().subscribe(
      (profile: Profile) => {
        this.profileForm.patchValue(profile);
        this.profilePhotoUrl = `http://localhost:8000${profile.photo}`;
      },
      error => {
        console.error('Error al cargar el perfil', error);
      }
    );
  }

  //Permitir editar perfil de usuario o no
  toggleEditing() {
    this.editing = !this.editing;
    if (this.editing) {
      this.profileForm.enable();
    } else {
      this.profileForm.disable();
    }
  }

  //Me permite buscar una imagen en mi pc
  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0] as File;
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

  uploadPhoto() {
    if (this.selectedFile) {
      this.profileService.uploadPhoto(this.selectedFile).subscribe(
        response => {
          this.loadUserProfile();
        },
        error => {
          console.error('Error al subir la foto', error);
        }
      );
    }
  }
}