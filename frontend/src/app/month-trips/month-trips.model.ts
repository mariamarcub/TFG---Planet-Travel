export interface Month {
    id: number; // Identificador único del mes (0 para enero, 1 para febrero, etc.)
    monthName: string; // Nombre del mes (opcional, para mostrar en la interfaz de usuario)
    selectedMonth: boolean; // Propiedad para indicar si este mes está seleccionado
}

export class Voyage { /*Se tiene que hacer una clase para poder instanciar cada viaje*/
    id: number = 0;
    city__name: string = '';
    date_start: string = '';
    date_end: string = '';
    description: string = '';
    itinerary: string = '';
    price: number = 0;
    maximum_travelers: number = 0;
}

