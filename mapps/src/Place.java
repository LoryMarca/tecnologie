import java.util.HashMap;
import java.util.Map;

import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class Place {
    private final HashMap<String, String> attributes = new HashMap<>();// creo una hashmap di oggetti di tipo string che sono i vari attributi all'interno del place
    private final HashMap<String, String> childs = new HashMap<>();//creo un hashmap di oggetti di tipo string che sono i vari childs all'interno del place

    public Place(Node place){//metodo che crea una nuova istanza di Place con i suoi attributi e i suoi childs

        NamedNodeMap attributi = place.getAttributes();//creo una variabile di tipo NamedNodeMap che contiene i nomi degli attributi del nodo
        for(int i = 0; i < attributi.getLength(); i++){//per ogni attributo del nodo
            Node n = attributi.item(i);//creo una variabile di tipo Node che contiene l'attributo del nodo
            attributes.put(n.getNodeName(), n.getNodeValue());//inserisco l'attributo del nodo nell'hashmap di attributi
        }


        NodeList figli = place.getChildNodes();//creo una variabile di tipo NodeList che contiene i nodi figli del nodo
        for(int i = 0; i < figli.getLength(); i++){//per ogni figlio del nodo
            Node n = figli.item(i);//creo una variabile di tipo Node che contiene l'figlio del nodo
            if(!n.getNodeName().equals("text#")){//se il figlio del nodo non è una stringa
                childs.put(n.getNodeName(), n.getTextContent());//inserisco l'attributo del nodo nell'hashmap di childs
            }
            
        }
        
    }

    @Override
    public String toString() {//metodo che restituisce una stringa che rappresenta l'oggetto Place
        String s = "";
        for (Map.Entry<String, String> entry : childs.entrySet()) {//per ogni entry dell'hashmap di childs
            s+=("Key : " + entry.getKey() + " Value : " + entry.getValue())+"\n";//aggiungo una stringa che rappresenta l'entry dell'hashmap di childs
        }
        return s;
    }
}
