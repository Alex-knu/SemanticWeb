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

@Component({
  selector: 'app-user-table',
  templateUrl: './user-table.component.html',
  styleUrls: ['./user-table.component.scss']
})

export class UserTableComponent {
  submitted: boolean;
  museum: MuseumModel;
  museum_url: string;

  constructor(private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.activatedRoute.queryParams.subscribe(params => {
      this.museum_url = params['museum_url'];
      console.log(this.museum_url);
    });
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

