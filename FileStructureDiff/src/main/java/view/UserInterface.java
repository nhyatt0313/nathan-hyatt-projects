package view;

import javax.swing.*;

public class UserInterface {

    public JFrame initialize(){
        JFrame frame = new JFrame("File Structure Diff");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1000, 300);
        JButton submit = new JButton("Diff Selected Paths");
        frame.getContentPane().add(submit);
        frame.setVisible(true);
        return frame;

    }
}
