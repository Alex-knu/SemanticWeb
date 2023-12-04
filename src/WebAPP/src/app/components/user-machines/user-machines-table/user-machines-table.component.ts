import { Component, OnInit } from '@angular/core';
import { MessageService } from 'primeng/api';
import { Table } from 'primeng/table';
import { DialogService, DynamicDialogRef } from 'primeng/dynamicdialog';
import { UserMachineInfoComponent } from '../user-machines-info/user-machines-info.component';
import { UserMachineExecuteCommandComponent } from '../user-machines-execute-command/user-machines-execute-command.component';
import { MuseumTableModel } from 'src/app/shared/models/museumTable.model';

@Component({
  selector: 'app-user-machines-table',
  templateUrl: './user-machines-table.component.html',
  styleUrls: ['./user-machines-table.component.scss']
})

export class UserMachineTableComponent {
  museums: MuseumTableModel[];
  ref: DynamicDialogRef;
  loading: boolean = true;
  machine: any;
  ukraine_regions = [
    'Вінницька область',
    'Волинська область',
    'Дніпропетровська область',
    'Донецька область',
    'Житомирська область',
    'Закарпатська область',
    'Запорізька область',
    'Івано-Франківська область',
    'Київська область',
    'Кіровоградська область',
    'Луганська область',
    'Львівська область',
    'Миколаївська область',
    'Одеська область',
    'Полтавська область',
    'Рівненська область',
    'Сумська область',
    'Тернопільська область',
    'Харківська область',
    'Херсонська область',
    'Хмельницька область',
    'Черкаська область',
    'Чернівецька область',
    'Чернігівська область',
    'м. Київ'
  ]

  constructor(
    private messageService: MessageService,
    private dialogService: DialogService) { }

  ngOnInit() {
    this.museums = [
      {
          museum: "Ладомирія",
          museum_type: "",
          museum_url: "http://www.wikidata.org/entity/Q111846032",
          region: "Рівненська область",
          settlement: "Радивилів"
      },
      {
          museum: "Зміївський краєзнавчий музей",
          museum_type: "краєзнавчий музей",
          museum_url: "http://www.wikidata.org/entity/Q111894861",
          region: "Харківська область",
          settlement: "Зміїв"
      }
    ];
  }



  clear(table: Table) {
    table.clear();
}

  // onClick(event: any) {
  //   event.changeValues = this.machines[0].changeValues;
  // }

  editMachine(machine: any) {
    this.machine = machine;

    this.ref = this.dialogService.open(UserMachineInfoComponent, {
      header: 'Деталі хоста',
      data: machine,
      contentStyle: { overflow: 'auto' },
      baseZIndex: 10000,
      maximizable: true
    });

    // this.ref.onClose.subscribe((application: BaseApplication) => {
    //   if (application && application.id) {
    //     this.baseApplicationService.collection.getAll()
    //       .subscribe(
    //         (applications) => {
    //           this.applications = applications;
    //         });

    //     this.messageService.add({ severity: 'info', summary: 'Список оновлено', detail: application.name });
    //   }
    // });
  }


  executeCommand(machine: any) {
    this.machine = machine;

    this.ref = this.dialogService.open(UserMachineExecuteCommandComponent, {
      header: 'Виконати команду',
      data: machine,
      contentStyle: { overflow: 'auto' },
      baseZIndex: 10000,
      maximizable: true
    });
  }

  openNew() {
    this.ref = this.dialogService.open(UserMachineInfoComponent, {
      header: 'Деталі хоста',
      contentStyle: { overflow: 'auto' },
      baseZIndex: 10000,
      maximizable: true
    });

    // this.ref.onClose.subscribe((application: BaseApplication) => {
    //   if (application && application.id) {
    //     this.baseApplicationService.collection.getAll()
    //       .subscribe(
    //         (applications) => {
    //           this.applications = applications;
    //         });

    //     this.messageService.add({ severity: 'info', summary: 'Список оновлено', detail: application.name });
    //   }
    // });
  }

}
