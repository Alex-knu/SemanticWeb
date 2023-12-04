import { Component, OnInit } from '@angular/core';
import { MessageService } from 'primeng/api';
import { Table } from 'primeng/table';
import { DialogService, DynamicDialogRef } from 'primeng/dynamicdialog';
import { UserMachineInfoComponent } from '../user-machines-info/user-machines-info.component';
import { UserMachineExecuteCommandComponent } from '../user-machines-execute-command/user-machines-execute-command.component';
import { MuseumTableModel } from 'src/app/shared/models/museumTable.model';
import { MuseumModel } from 'src/app/shared/models/museum.model';
import { Router } from '@angular/router';
import { MuseumTableService } from 'src/app/shared/services/api/museumTable.service';

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

  constructor(
    private messageService: MessageService,
    private dialogService: DialogService,
    private router: Router,
    private museumTableService: MuseumTableService) { }

  ngOnInit() {
    this.museumTableService.collection.getAll().subscribe(
      museums => {
        this.museums = museums;
      });
  }



  clear(table: Table) {
    table.clear();
  }

  // onClick(event: any) {
  //   event.changeValues = this.machines[0].changeValues;
  // }

  openFullInfo(museum: MuseumModel) {
    this.router.navigate(['/user/user-table'], { queryParams: { museum_url: museum.museum_url } });
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
