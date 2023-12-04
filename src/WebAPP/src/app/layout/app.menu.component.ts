import { OnInit } from '@angular/core';
import { Component } from '@angular/core';
import { LayoutService } from './service/app.layout.service';
import { AuthService } from '../shared/services/auth.service';
import { ROLE_ADMIN, ROLE_EVALUATOR, ROLE_USER } from '../shared/constants';

@Component({
  selector: 'app-menu',
  templateUrl: './app.menu.component.html'
})

export class AppMenuComponent implements OnInit {
  admin = ROLE_ADMIN;
  evaluator = ROLE_EVALUATOR;
  user = ROLE_USER;

  model: any[] = [];

  constructor(
    public layoutService: LayoutService,
    public authService: AuthService) { }

  ngOnInit() {
    this.model = [
      {
        label: 'Головна',
        visible: true,
        items: [
          {
            label: 'Головна',
            icon: 'pi pi-fw pi-home',
            routerLink: ['/']
          }
        ]
      },
      {
        label: 'Музеї',
        visible: this.isVisible(this.user),
        items: [
          {
            label: 'Музеї',
            icon: 'pi pi-fw pi-desktop',
            routerLink: ['/user-machines/museum-table'],
            visible: this.isVisible(this.user)
          }
        ]
      },
      {
        label: 'Адміністрування',
        visible: this.isVisible(this.admin),
        items: [
          {
            label: 'Синхронізація',
            icon: 'pi pi-fw pi-desktop',
            routerLink: ['/user/synhronize'],
            visible: this.isVisible(this.admin)
          }
        ]
      }
    ];
  }

  isVisible(role: string): boolean {
    return this.authService.checkRole(role);
  }
}
