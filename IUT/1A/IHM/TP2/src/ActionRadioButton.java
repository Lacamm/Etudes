import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.RadioButton;

public class ActionRadioButton implements EventHandler<ActionEvent>{
    private CalculetteV2 appli ;
    public ActionRadioButton(CalculetteV2 appli)
    {
        this.appli = appli ;
    }
    public void handle(ActionEvent actionEvent)
    {
        RadioButton r = (RadioButton) actionEvent.getSource();
        switch(r.getText()){
            case "addition":this.appli.getButton().setText("+");break;
            case "soustraction":this.appli.getButton().setText("-");break;
            case "multiplication":this.appli.getButton().setText("*");break;
            case "division":this.appli.getButton().setText("/");break;
        }
    }
}
