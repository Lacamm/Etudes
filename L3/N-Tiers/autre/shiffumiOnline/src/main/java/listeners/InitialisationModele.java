package listeners;

import modele.FacadeShiffumi;
import modele.FacadeShiffumiImpl;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;

public class InitialisationModele implements ServletContextListener {

    @Override
    public void contextInitialized(ServletContextEvent servletContextEvent) {

        FacadeShiffumi facadeShiffumi = new FacadeShiffumiImpl();

        servletContextEvent.getServletContext().setAttribute("facade",facadeShiffumi);
    }

    @Override
    public void contextDestroyed(ServletContextEvent servletContextEvent) {

    }
}
