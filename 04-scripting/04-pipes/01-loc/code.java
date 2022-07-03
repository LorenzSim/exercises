package ui;

import domain.*;

import java.time.LocalDate;

public class Appeke {
    public static void main(String[] args){

        Winkel winkel = new Winkel();

        // 2 boeken
        Product harryPotter = new Boek("Harry Potter", new Euro(19, 95), 20, 1);
        Product grijzeJager = new Boek("De grijze Jager", new Euro(15, 49), 15, 3);

        // 2 weekbladen
        Product dagAllemaal = new Weekblad("Dag allemaal!", new Euro(3, 99), 30, LocalDate.now());
        Product libelle = new Weekblad("Libelle", new Euro(2, 5), 25, LocalDate.of(2022, 2, 24));

        // producten toevoegen aan de winkelvoorraad
        winkel.voegProductToe(harryPotter);
        winkel.voegProductToe(grijzeJager);
        winkel.voegProductToe(dagAllemaal);
        winkel.voegProductToe(libelle);

        // info producten tonen
        for(Product p : winkel.getProducten()){
            System.out.println(p.geefInfo());
        }

        // voorraad wijzigen
        winkel.veranderVoorraadVan(harryPotter, 19);
        winkel.veranderVoorraadVan(grijzeJager, 13);
        winkel.veranderVoorraadVan(dagAllemaal, 29);
        winkel.veranderVoorraadVan(libelle, 30);


    }
}

