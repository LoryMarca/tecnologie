import java.io.IOException;
import java.util.ArrayList;

import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

public class App {
    // creo il link da dove poi scaricherò il file json
    private final static String inizio = "https://nominatim.openstreetmap.org/search?q=";
    private final static String fine = "&format=xml&polygon_geojson=1&addressdetails=1";

    private static String daStampare="";

    public static void main(String[] args) throws Exception {

        String ricerca = "mariano+comense;+monnet";// questa è la ricerca che faccio nel file json

        String source = inizio + ricerca + fine;// aggiungo linizio del link con la ricerca da fare per poi finire con la fine del link
        // la sctringa souce ora è il link per intero
        // System.out.println(source);

        String file = "";
        try {
            file = XMLReader.fetchFromWeb(source);// richiamo la funzione che mi permette di scaricare il file json
            XMLReader.printToFile(file, "data.xml");// scrivo il file json nel file data.xml
        } catch (IOException e1) {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }

        Element root = XMLReader.getRootElementFromXML("data.xml");// richiamo la funzione che mi permette di leggere il file xml
        // così facendo trovo la root del file xml e la metto nella variabile root

        NodeList Childs = root.getElementsByTagName("place");// richiamo la funzione che mi permette di leggere il file xml
        // così facendo trovo i vari figlio all'interno della root(chiamati place in
        // questo xml) e li metto nella variabile childs

        ArrayList<Place> lista = new ArrayList<Place>();// creo una lista di oggetti di tipo Place

        for (int i = 0; i < Childs.getLength(); i++) {// scorro ogni figlio trovato
            lista.add(new Place(Childs.item(i)));// aggiungo tutti i vari figlio ad una lista di oggetti di tipo Place
        }

        System.out.println(lista.get(0));// stampo la prima posizione della lista di oggetti di tipo Place

        String stampa =lista.get(0).toString();

        visualizzaFinestra();// chiamo la funzione che mi permette di visualizzare la finestra

        //stampare(stampa);

    }

    public static void visualizzaFinestra() {
        NewJFrame frame = new NewJFrame();// creo un nuovo frame
        frame.setVisible(true);// imposto la visibilità del frame a true

    }

    public String stampare(String s) {
        daStampare = s;
        return daStampare;
    }
}
