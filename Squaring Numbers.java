import java.util.List;
import java.util.ArrayList;

public class Main {

    public static List<Integer> squaredList(List<Integer> list) {
        for (int i = 0; i < list.size(); i++) { // Schleife über die Liste
            list.set(i, list.get(i) * list.get(i)); // Quadrat der Zahl setzen
        }
        return list;
    }

    public static void main(String[] args) {
        List<Integer> list = new ArrayList<Integer>();

        list.add(1);
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(5);
        list.add(8);
        list.add(13);
        list.add(21);
        list.add(34);
        list.add(55);

        //Funktion
        list = squaredList(list);
        System.out.println(list);
    }
}
