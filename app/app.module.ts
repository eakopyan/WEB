import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { EtudiantsComponent } from './etudiants/etudiants.component';
import { FormsModule } from '@angular/forms';
import { DetailEtudiantComponent } from './detail-etudiant/detail-etudiant.component';
import { EtudiantsService } from './etudiants.service';

@NgModule({
  declarations: [
    AppComponent,
    EtudiantsComponent,
    DetailEtudiantComponent
  ],
  imports: [
    BrowserModule,
    BrowserModule,
    FormsModule
  ],
  providers: [EtudiantsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
