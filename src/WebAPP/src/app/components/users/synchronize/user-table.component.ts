import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MuseumModel } from 'src/app/shared/models/museum.model';
import { MuseumService } from 'src/app/shared/services/api/museum.service';
import { SynhronizeService } from 'src/app/shared/services/api/synhronize.service';
import { MessageService } from 'primeng/api';

@Component({
  selector: 'app-user-table',
  templateUrl: './user-table.component.html',
  styleUrls: ['./user-table.component.scss']
})

export class SynhronizeComponent {
  constructor(private activatedRoute: ActivatedRoute,
    private synhronizeService: SynhronizeService,
    private messageService: MessageService,) { }

  ngOnInit(): void {
  }

  synhronize(): void {
    this.synhronizeService.single.create({}).subscribe(
         () => {
           this.messageService.add({ severity: 'success', summary: 'Successful', detail: 'Синхронізовано' });
         },
         error => {
           this.messageService.add({ severity: 'error', summary: 'Error', detail: 'Error' });
         });
  }
}

