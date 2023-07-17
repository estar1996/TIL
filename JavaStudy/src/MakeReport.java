public class MakeReport {

    StringBuffer buffer = new StringBuffer();

    private String line = "=============";
    private String title = "이름\t 주소\t\t 전화번호 \n";
    private void makeHeader() {
        buffer.append(line);
        buffer.append(title);
        buffer.append(line);
    }

    private void generateBody() {
        buffer.append("Jame\t");
    }

}
