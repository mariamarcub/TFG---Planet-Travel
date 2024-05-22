import { Component, OnInit, OnDestroy, ViewChild, ElementRef } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { BookingService } from './booking.service';
import { ActivatedRoute, Params, Router } from '@angular/router';  // Importar Router
import { loadStripe, Stripe, StripeCardElement } from '@stripe/stripe-js';

@Component({
  selector: 'app-booking',
  templateUrl: './booking.component.html',
  styleUrls: ['./booking.component.css']
})
export class BookingComponent implements OnInit, OnDestroy {
  @ViewChild('cardElement') cardElement!: ElementRef;
  stripe: Stripe | null = null;
  card!: StripeCardElement;
  cardErrors?: string;
  bookingForm: FormGroup;
  voyageId?: number;
  numPersons?: number;
  voyagePrice?: number;
  isDataLoaded: boolean = false;

  constructor(
    private formBuilder: FormBuilder,
    private bookingService: BookingService,
    private route: ActivatedRoute,
    private router: Router  // Inyectar Router
  ) {
    this.bookingForm = this.formBuilder.group({
      name: ['', Validators.required],
      last_name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      birth_date: ['', Validators.required],
      telephone: ['', [Validators.required, Validators.pattern(/^[0-9]{9}$/)]],
      dni: [''],
      passport: [''],
      departure_city: ['', Validators.required],
    });
  }

  async ngOnInit() {
    this.route.params.subscribe((params: Params) => {
      this.voyageId = +params['voyage'];
      this.numPersons = +params['numPersons'];
      this.voyagePrice = +params['voyagePrice'];
      this.isDataLoaded = true;
    });

    this.stripe = await loadStripe('pk_test_51PIvXSGtzfLtviFbGNjVx8NNaZ3TnNo6B6gciAXuUop3PbeWOWyouDErFga0GYm2bZJ6BW09OTV18A3Qq69Czp1c00S3FTXfWO');
    if (this.stripe) {
      const elements = this.stripe.elements();
      this.card = elements.create('card');
      this.card.mount(this.cardElement.nativeElement);

      this.card.on('change', (event) => {
        this.cardErrors = event.error ? event.error.message : '';
      });
    } else {
      console.error('Stripe no se pudo cargar');
    }
  }

  ngOnDestroy() {
    if (this.card) {
      this.card.destroy();
    }
  }

  async onSubmit() {
    if (this.bookingForm.valid) {
      const formData = {
        ...this.bookingForm.value,
        voyageId: this.voyageId
      };

      if (this.stripe) {
        const { token, error } = await this.stripe.createToken(this.card);
        if (error) {
          this.cardErrors = error.message;
        } else {
          formData['stripeToken'] = token.id;
          console.log('Formulario válido', formData);
          this.bookingService.createPurchase(formData).subscribe({
            next: response => {
              console.log('Respuesta del servidor:', response);
              this.router.navigate(['/']);  // Redirigir a la ruta de cabecera después de una compra exitosa
            },
            error: error => {
              console.error('Error al crear la compra', error);
            }
          });
        }
      } else {
        console.error('Stripe no está inicializado');
      }
    } else {
      console.log('Formulario inválido');
    }
  }
}
