import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { SynhronizeComponent } from './user-table.component';

@NgModule({
  imports: [RouterModule.forChild([
    { path: '', component: SynhronizeComponent }
  ])],
  exports: [RouterModule]
})

export class SynhronizeRoutingModule { }
