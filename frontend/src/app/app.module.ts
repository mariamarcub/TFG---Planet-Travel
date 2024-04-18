import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { ContinentComponent } from './continent/continent.component';
import { CabeceraComponent } from './cabecera/cabecera.component';
import { RouterModule, Routes } from '@angular/router';
import { FooterComponent } from './footer/footer.component';
import { MonthsComponent } from './months/months.component';
import { AgeGroupComponent } from './age-group/age-group.component';
import { LoginComponent } from './login/login.component'; 
import { AppRoutingModule } from './app-routing.module'; 
import { FormsModule } from '@angular/forms'; // Importa FormsModule



const routes: Routes = [
  { path: 'continents', component: ContinentComponent }
];


@NgModule({
  declarations: [
    AppComponent,
    CabeceraComponent,
    ContinentComponent,
    FooterComponent,
    MonthsComponent,
    AgeGroupComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
   // RouterModule.forRoot(routes),
    AppRoutingModule, 
    FormsModule //Para poder hacer los formularios y recoger los datos de django


  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
