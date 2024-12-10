import java.util.ArrayList;
import java.util.List;

public class MemoryLeakExample {
    static List<String> memoryLeakList = new ArrayList<>();

    public static void main(String[] args) {
        for (int i = 0; i < 1000000; i++) {
            addToMemoryLeakList("Leak " + i);
            if (i % 100000 == 0) {
                System.out.println("Added " + i + " items to the list");
            }
        }
        System.out.println("Memory leak example finished.");
    }

    public static void addToMemoryLeakList(String value) {
        // Objects added to this list will not be garbage collected
        memoryLeakList.add(value);
    }
}

