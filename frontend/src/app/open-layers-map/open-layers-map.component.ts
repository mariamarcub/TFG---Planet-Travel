import { Component, Input, OnInit, SimpleChanges } from '@angular/core';
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import { fromLonLat } from 'ol/proj';
import OSM from 'ol/source/OSM';

@Component({
  selector: 'open-layers-map',
  templateUrl: './open-layers-map.component.html',
  styleUrls: ['./open-layers-map.component.css'],
})
export class OpenLayersMapComponent implements OnInit {
  @Input() latitud: number = 37.38283;
  @Input() longitud: number = -5.97317;

  map!: Map;

  ngOnInit(): void {
    debugger;
    this.map = new Map({
      view: new View({
        center: fromLonLat([this.longitud, this.latitud]),
        zoom: 10, // Ajusta el nivel de zoom según sea necesario
      }),
      layers: [
        new TileLayer({
          source: new OSM(),
        }),
      ],
      target: 'ol-map'
    });
  }
}
