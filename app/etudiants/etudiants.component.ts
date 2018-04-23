import { Component, OnInit } from '@angular/core';
import { EtudiantsService } from '../etudiants.service'


@Component({
  selector: 'app-etudiants',
  templateUrl: './etudiants.component.html',
  styleUrls: ['./etudiants.component.css']
})

export class EtudiantsComponent implements OnInit {
  etudiants = [];
  lEtudiant:any;

  onSelect(etudiant) {
    this.lEtudiant = etudiant ;
  }

  getEtudiants() {
    this.etudiantsService.getEtudiants().subscribe(etudiants => this.etudiants = etudiants);
  }

  constructor(private etudiantsService: EtudiantsService) { }

  ngOnInit() {
    this.getEtudiants();
  }

}
