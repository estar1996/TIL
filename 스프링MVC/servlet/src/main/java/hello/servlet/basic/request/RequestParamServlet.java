package hello.servlet.basic.request;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Enumeration;

/**
 * http://localhost:8080/request-param?username=hello&age=20
 */
@WebServlet(name = "requestParamServlet",urlPatterns = "/request-param")
public class RequestParamServlet extends HttpServlet {

    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("RequestParamServlet.service");
        request.getParameterNames();
        System.out.println("[단일조회]");
        String username = request.getParameter("username");
        String age = request.getParameter("age");

//        super.service(request,response);
    }
}
