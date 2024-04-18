import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CabeceraComponent } from './cabecera/cabecera.component';
import { LoginComponent } from './login/login.component';


const routes: Routes = [
  { path: '', component: CabeceraComponent },
  { path: 'login', component: LoginComponent } //Definimos la ruta para poder ir al HTML del componente login
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
