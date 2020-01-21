package view;

import javax.swing.*;

public class UserInterface {

    public JFrame initialize(){
        // Frame
        JFrame frame = new JFrame("File Structure Diff");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(1000, 500);


        // Text Fields for entering file paths
        JPanel pathsPanel = new JPanel();
        JTextField path1 = new JTextField();
        JTextField path2 = new JTextField();
        pathsPanel.add(path1);
        pathsPanel.add(path2);


        // Submit Button and Panel
        JPanel buttonPanel = new JPanel();
        JButton submit = new JButton("Submit");
        submit.setSize(50, 20);
        buttonPanel.add(submit);



        // Assemble Pieces
        frame.getContentPane().add(buttonPanel);
        frame.getContentPane().add(pathsPanel);

        // Location and visibility
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        return frame;

    }
}
