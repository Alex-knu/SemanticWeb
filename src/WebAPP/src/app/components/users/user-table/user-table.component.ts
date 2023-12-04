import { Component } from '@angular/core';
import { Router, ActivatedRoute, Params } from '@angular/router';
import { MessageService, ConfirmationService } from 'primeng/api';
import { DynamicDialogRef, DialogService } from 'primeng/dynamicdialog';
import { UserInfoModel } from 'src/app/shared/models/userInfo.model';
import { UserService } from 'src/app/shared/services/api/user.service';
import { AuthService } from 'src/app/shared/services/auth.service';
import { UserInfoComponent } from '../user-info/user-info.component';
import { MuseumModel } from 'src/app/shared/models/museum.model';
import { DOCUMENT } from '@angular/common';
import { MuseumService } from 'src/app/shared/services/api/museum.service';

@Component({
  selector: 'app-user-table',
  templateUrl: './user-table.component.html',
  styleUrls: ['./user-table.component.scss']
})

export class UserTableComponent {
  submitted: boolean;
  museum: MuseumModel;
  museum_url: string;

  constructor(private activatedRoute: ActivatedRoute,
    private museumService: MuseumService) { }

  ngOnInit(): void {
    this.activatedRoute.queryParams.subscribe(params => {
      this.museumService.single.create({"museum_url": params['museum_url']}).subscribe(
        museum => {
          this.museum = museum;
        });
      });
  }

  openWikiDataUrl(): void {
    (window as any).open(this.museum.museum_url, "_blank");
  }

  openWebSiteUrl(): void {
    (window as any).open(this.museum.site, "_blank");
  }

  openMapUrl(): void {
    (window as any).open(this.museum.map_link, "_blank");
  }
}

