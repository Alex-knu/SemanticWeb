import { Component } from '@angular/core';
import { UUID } from 'angular2-uuid';
import { MessageService } from 'primeng/api';
import { DialogService, DynamicDialogConfig, DynamicDialogRef } from 'primeng/dynamicdialog';
import { MuseumModel } from 'src/app/shared/models/museum.model';

@Component({
  selector: 'app-user-machines-info',
  templateUrl: './user-machines-info.component.html',
  styleUrls: ['./user-machines-info.component.scss']
})

export class UserMachineInfoComponent {
  submitted: boolean;
  museum: MuseumModel;

  constructor(
    private messageService: MessageService,
    public dialogService: DialogService,
    public ref: DynamicDialogRef,
    public config: DynamicDialogConfig) { }

  ngOnInit(): void {
    this.museum =
    {
      adress: "с. Хоросно, Львівська область, Україна",
      geo: "(23.985277777, 49.654722222)",
      inception: "2020-11-01T00:00:00Z",
      map_link: "https://www.google.com/maps?ll=49.654722222,23.985277777.531111&q=49.654722222,23.985277777&hl=en&t=m&z=11",
      museum: "Музей загиблих літаків",
      museum_type: "",
      museum_url: "http://www.wikidata.org/entity/Q105751941",
      region: "Львівська область",
      settlement: "Хоросно",
      site: ""
    };
  }
}
