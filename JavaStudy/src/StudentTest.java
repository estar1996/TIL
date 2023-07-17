public class StudentTest {

    public static void main(String[] args) {
        Student studentLee = new Student();
        studentLee.studentName = "이순신";
        studentLee.address = "서울";

        studentLee.showStudentInfo();
        System.out.println(studentLee);

    }
}
