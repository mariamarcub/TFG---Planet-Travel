import { LOCALE_ID, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { ContinentComponent } from './continent/continent.component';
import { CabeceraComponent } from './cabecera/cabecera.component';
import { Routes } from '@angular/router';
import { FooterComponent } from './footer/footer.component';
import { MonthsComponent } from './months/months.component';
import { AgeGroupComponent } from './age-group/age-group.component';
import { LoginComponent } from './login/login.component'; 
import { AppRoutingModule } from './app-routing.module'; 
import { FormsModule, ReactiveFormsModule } from '@angular/forms'; // Importa FormsModule
import { LoginInterceptor } from './shared/common-interceptor';
import { MonthTripsComponent } from './month-trips/month-trips.component';
import { ProfileComponent } from './profile/profile.component';
import { BodyComponent } from './body/body.component';
import { VoyageComponent } from './voyage/voyage.component';
import { registerLocaleData } from '@angular/common';
import localeEs from '@angular/common/locales/es';
import { OpenLayersMapComponent } from './open-layers-map/open-layers-map.component';
import { BookingComponent } from './booking/booking.component';

// Registra el idioma español
registerLocaleData(localeEs);

const routes: Routes = [
  { path: 'continents', component: ContinentComponent, },
  { path: 'map', component: OpenLayersMapComponent, }
];


@NgModule({
  declarations: [
    AppComponent,
    CabeceraComponent,
    ContinentComponent,
    FooterComponent,
    MonthsComponent,
    AgeGroupComponent,
    LoginComponent,
    MonthTripsComponent,
    ProfileComponent,
    BodyComponent,
    VoyageComponent,
    OpenLayersMapComponent,
    BookingComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
   // RouterModule.forRoot(routes),
    AppRoutingModule, 
    FormsModule, //Para poder hacer los formularios y recoger los datos de django,
    ReactiveFormsModule
  ],
  providers: [
                { provide: HTTP_INTERCEPTORS, useClass: LoginInterceptor, multi: true },
                { provide: LOCALE_ID, useValue: 'es' }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }