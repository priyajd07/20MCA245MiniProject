import java.io.*;
import java.net.*;
import javax.swing.*;
import javax.swing.event.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.event.*;
import javax.swing.border.* ;
import javax.swing.text.AbstractDocument;
import javax.swing.text.AttributeSet;
import javax.swing.text.BadLocationException;
import javax.swing.text.DocumentFilter;


class  CharShape
  {              
  
   boolean Rslt = false ;
   int Bcnt,Sub1,Sub2;
   String CurrType = "";
   char Kc;   
   int Store[][] = new int[80][8];


   private JFrame             FrameArr;
   private JPanel             PanelArr;
   private JLabel             PanLabel;

   private JTextField         TextArr[][] = new JTextField[8][8]; 
   private JTextField         TextChr;

   private JButton            ButtonArr[] = new JButton[3] ;

   //---------- Opn file and connect to stream-----------------------------------------------------
  public  void Design() 
  {

     String Fn = "chardot.bin";
     Create_frame(100,100,600,540," "); 
     Create_panel( 0,0,600,540,"DRAW CHARACTERS ");         
     Create_TextField ();     
     
     Create_Button ( 250,375,100,25, "Save" , 0);
     Create_Button ( 150,450,100,25, "Clear" , 1);
     Create_Button ( 350,450,100,25, "Exit" , 2);

     FrameArr.revalidate();
     FrameArr.repaint();

     TextChr.grabFocus();

     Rslt =  ReadFile (Fn );

     CurrType ="*";

     while ( true ) 
     {

System.out.println(Sub1+CurrType+Sub2);

        if (CurrType.equals("B") && Sub1 == 2 )
            break;
 
            
        if (CurrType.equals("B") && Sub1 == 1 ) {
            Clear_Screen();
            CurrType ="*";
        }                          


        if (CurrType.equals("B") && Sub1 == 0 ) {
            ToStore();
            Clear_Screen();
            CurrType ="*";
        }                          
        

        if (CurrType.equals("T") && Sub1 < 8  && (Kc == '0' || Kc == '1')   ) 
          {
System.out.println(Sub1+CurrType+Sub2);
            TextArr[Sub1][Sub2].setText(" ");

            TextArr[Sub1][Sub2].setText("");

            if ( Kc == '0')
               TextArr[Sub1][Sub2].setText("0");
            else if ( Kc == '1')
               TextArr[Sub1][Sub2].setText("1");
            
            Sub2 = Sub2 + 1;

            if (Sub2 == 8 ) {
               Sub1=Sub1+1;
               Sub2=0;
            }   
  
            if (Sub1 == 8 ) {
               Sub1=0;
               Sub2=0;
            }   
            
            TextArr[Sub1][Sub2].grabFocus();
            CurrType ="*";
       }
         
       if (CurrType.equals("T") && Sub1 == 8  && Kc >= '0' && Kc <= '~')  {             
System.out.println(Sub1+CurrType+Sub2);
          FromStore();       
          TextArr[0][0].grabFocus();
          CurrType ="*";
       }
     }
     
System.out.println("exit");
     Rslt =  WriteFile (Fn);
     FrameArr.dispose();
  }

// ------------------------------------------Clear Screen---------------------------------------
 private  void Clear_Screen() 
  {
       for (int Tptr = 0 ; Tptr < 8 ; Tptr++) 
         {
             for (int T2 = 0 ; T2 < 8 ; T2++) 
               {
                   TextArr[Tptr][T2].setText("");
          }
       }      
       TextChr.setText("");
       TextChr.grabFocus();
}
//---------- get the dots for the char to screen --------------
private void FromStore() 
  {
    int  Cnt ,Pnt;
    String Str = TextChr.getText();
System.out.println(Str);

    char character = Str.charAt(0); 
    int ch = (int) character - 48;

System.out.println(ch);

    for ( int i = 0 ; i < 8 ; i++)
    {
      Pnt = Store[ch][i];
      Cnt = 128;
   
System.out.println(i+" "+Pnt+" "+ Cnt);      
     
      for ( int j = 0 ; j < 8 ;j++)
      { 
        TextArr[i][j].setText("");

        if ( Pnt >= Cnt ) { 
           TextArr[i][j].setText("1");
           Pnt = Pnt - Cnt;
        }   
        else
           TextArr[i][j].setText("0");
        
        Cnt = Cnt / 2;   
      }
      System.out.println( Pnt +" "+ Cnt);         

    }
 }
 //---------- Store the dots for edited char-----------------------------------------------------
  private  void ToStore() 
  {
    String Str = TextChr.getText();
    char character = Str.charAt(0); 
    int Pnt = (int) character - 48 , Cnt=0 , Val=0;

System.out.println("tostoree");

    for ( int i = 0 ; i < 8 ; i++)
    {
   	
      Val = 0;
      Cnt = 128;

      
      for ( int j = 0 ; j < 8 ;j++)
      { 
System.out.println(Cnt);
        if (TextArr[i][j].getText().equals("1"))   
           Val = Val + Cnt;
        
        Cnt = Cnt / 2;   
      }
      
      Store[Pnt][i] = Val;
System.out.println(Pnt+" "+i+" "+ Store[Pnt][i]);
    }
System.out.println("Saved");

 }
   //---------- Opn file and connect to stream-----------------------------------------------------
  private  boolean ReadFile (String Nam ) 
  {
      File Fil;
      BufferedInputStream Bf = null;
      byte[] Bt = new byte[640];
      int Cnt=0;
      boolean Opened = false;

      try
      {
        Fil = new File(Nam);
        Bf = new BufferedInputStream(new FileInputStream(Fil));
        Opened = true;        
      } catch (IOException e)
      {
         
      }
      
      
      if (Opened )
      {
          try {
             Bcnt =  Bf.read(Bt , 0 , 640 );
             Bf.close();
          }   
           catch ( Exception e)
            {
              System.out.println("File Reading error ");
            }
       }
              
       Bcnt = Bcnt/ 8;
       Cnt  = 0;
       
       for ( int i=0; i < Bcnt ;  i++)
        {
          for ( int j = 0 ; j < 8 ;j++)
          { 
            Store[i][j] = Bt[Cnt] & 0xff;
            Cnt++;  
          }
       }         

       Bcnt = 80 - Bcnt;

       for ( int i=0; i < Bcnt ;  i++)
        {
          for ( int j = 0 ; j < 8 ;j++)
          { 
            Store[i][j] = 0;  
          }
       }         


       return true;
   }
 //----------  Read file-------------------------------------------------------------------------
  private boolean WriteFile (String Nam )
   {   	
      File Fil;

      BufferedOutputStream Bf = null;
      byte[] Bt = new byte[640];
      int Cnt=0;
      boolean Opened = false;
            
      try
      {
        Fil = new File(Nam);
        Bf = new BufferedOutputStream(new FileOutputStream(Fil));
        Opened = true;        
      } catch (IOException e)
      {
          System.out.println("file not opened");         
      }
   	
   	  if ( Opened )   {
         Bcnt = 80;
         Cnt  = 0;
       
         for ( int i=0; i < Bcnt ;  i++)
         {
            for ( int j = 0 ; j < 8 ;j++)
             { 
               Bt[Cnt] = (byte) Store[i][j];
               Cnt = Cnt +1;  
             }
         }         
   	
         try {
            Bf.write(Bt , 0 , 640 );
         }   
         catch ( Exception e)
           {
             System.out.println("File writing error ");
             return false;
         }
      }
      
      try {    
         Bf.flush();
         Bf.close();
      }
      catch (Exception e)
      {}
      
      return true;
   }  
//---Create Frame---------------------------------------------------------------
   private void Create_frame(int x,int y,int w,int h,String Lbl)  
     {            
      FrameArr= new JFrame();
      FrameArr.setLayout(null);
  	  FrameArr.setVisible(true);
      FrameArr.setBounds(x,y,w,h);
      FrameArr.setResizable(false);
      FrameArr.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
      FrameArr.setTitle(Lbl);
   }
//---Create Panel---------------------------------------------------------------   
   private void Create_panel(int x,int y,int w,int h,String Lbl)  
     {
      int Lw;
      PanelArr= new JPanel(); 
      PanelArr.setLayout(null);
      PanelArr.setVisible(true);
      PanelArr.setBounds(x,y,w,h);
      
      Lw = 10 * Lbl.length();   
      PanLabel = new JLabel();
      PanLabel.setSize(Lw,25);
      PanLabel.setLocation(0,0); 
      PanelArr.add(PanLabel);
      PanLabel.setText(Lbl);
         
      FrameArr.add(PanelArr);
  }  
//---Create TextField--------------------------------------------------------------------------------------  
   private void Create_TextField ()
     {
      int xx=300,yy=100,w=15,h=15;
      int  x , y=yy;	
     	
      for (int Tptr = 0 ; Tptr < 8 ; Tptr++) 
      {
      	x=xx;
      	
      	for (int T2 = 0 ; T2 < 8 ; T2++) 
         {
	  
   	       TextArr[Tptr][T2] = new JTextField();

           TextArr[Tptr][T2].setBounds(x,y,w,h);
           TextArr[Tptr][T2].setLayout(null);      
  	       TextArr[Tptr][T2].setFocusTraversalKeysEnabled(true);
  	       TextArr[Tptr][T2].setFocusTraversalPolicyProvider(false);
           TextArr[Tptr][T2].addActionListener(new ProgramEvents());
           TextArr[Tptr][T2].addKeyListener(new ProgramEvents());
           TextArr[Tptr][T2].setForeground(Color.RED);        
           TextArr[Tptr][T2].setBackground(Color.WHITE);        



           TextArr[Tptr][T2].putClientProperty("Ind","T" + String.format("%1s",Tptr) + String.format("%1s",T2)    );
           PanelArr.add(TextArr[Tptr][T2]);
           TextArr[Tptr][T2].setVisible(true);
           x=x+15;
          }
          y=y+h;
       }
       
       
       TextChr = new JTextField();

       TextChr.setBounds( xx,  yy - 50,20,25);
       TextChr.setLayout(null);      
       TextChr.setFocusTraversalKeysEnabled(true);
       TextChr.setFocusTraversalPolicyProvider(false);
       TextChr.putClientProperty("Ind","T88");
       TextChr.addActionListener(new ProgramEvents());
       TextChr.addKeyListener(new ProgramEvents());       
       PanelArr.add(TextChr);
       TextChr.setVisible(true);
  }     
//---Create Button--------------------------------------------------------------   
   private void Create_Button (int x,int y,int w,int h,String Lbl,int Bt)
     {
   	  ButtonArr[Bt]= new JButton(Lbl);
   	  ButtonArr[Bt].setHorizontalAlignment(SwingConstants.CENTER);
   	  ButtonArr[Bt].setBounds(x,y,w,h);
      ButtonArr[Bt].setVisible(true);
      
      ButtonArr[Bt].putClientProperty("Ind","B" + String.format("%1s",Bt) + "0");
           
      Border raisedBorder = BorderFactory.createRaisedBevelBorder();
      ButtonArr[Bt].setBorder(raisedBorder);
      ButtonArr[Bt].addMouseListener(new MovingAdapter());
      ButtonArr[Bt].addActionListener(new ProgramEvents());
      ButtonArr[Bt].addKeyListener(new ProgramEvents());
      PanelArr.add(ButtonArr[Bt]);

   }     
//-----------------------------------------------------------------------
private class ProgramEvents implements KeyListener,ActionListener
{
//implements FocusListener, KeyListener,ActionListener,ItemListener
//                                        ,TreeSelectionListener

//---ActionPerformed------------------------------------------------------------
   public void actionPerformed(ActionEvent e) 
     {      
     } 
//---keyPressed-----------------------------------------------------------------
   public void keyTyped(KeyEvent e) 
     {
   	  String Val="",act="",IndStr=" ";
   	  int Ln=0,KeyInx=0;
      boolean TmpBool=false; 

      //Ptr is used to store the Genptr of the field in which key is pressed. This should be preserved
      //till the end of the routine and hence it should not be used for any other purpose
      
      act = e.getSource().getClass().toString();
      KeyInx = e.getKeyCode();
      Kc     = e.getKeyChar();
      
      if( act.equals("class javax.swing.JButton"))	{
         JButton btn = (JButton) e.getSource();
         IndStr      = btn.getClientProperty("Ind").toString();

//System.out.println("Buuton pressed " + IndStr);

         if ( IndStr.length() > 2) {

         Sub1        = Integer.valueOf(IndStr.substring(1,2));
         Sub2        = Integer.valueOf(IndStr.substring(2,3));
         CurrType= "B";}
 
         
       }

      if (act.equals("class javax.swing.JTextField") )	{     	     
     	             JTextField Tx = (JTextField) e.getSource();
  	                 IndStr        = Tx.getClientProperty("Ind").toString();
                if ( IndStr.length() > 2) {
                     Sub1 = Integer.valueOf(IndStr.substring(1,2));
                     Sub2 = Integer.valueOf(IndStr.substring(2,3));
                     CurrType    = "T";}
  	 }                     
//  System.out.println("Text entered " + IndStr);

  }
//---keyReleased----------------------------------------------------------------
   public void keyReleased(KeyEvent e) 
     {
     }
//---keyTyped-------------------------------------------------------------------
   public void keyPressed(KeyEvent e) 
   {  
     } 
//---valueChanged---------------------------------------------------------------
   public void valueChanged(TreeSelectionEvent event) 
     {
     }
//---tableChanged---------------------------------------------------------------
   public void tableChanged(TableModelEvent e)
     {
     }
 } //-------  End Of Event Class     


//------------------------ Mouse events ---------------------
 class MovingAdapter extends MouseAdapter {
    public void mouseDragged(MouseEvent e) {
    } 
    
    public void mouseClicked(MouseEvent e) {
       String IndStr,act = e.getSource().getClass().toString();
      
       
      if( act.equals("class javax.swing.JButton"))	{
         JButton btn = (JButton) e.getSource();
         IndStr      = btn.getClientProperty("Ind").toString();
         if ( IndStr.length() > 2) {

         Sub1        = Integer.valueOf(IndStr.substring(1,2));
         Sub2        = Integer.valueOf(IndStr.substring(2,3));
         CurrType= "B";}
      }
              	         	                      
     }
  }
    
//-----------------------------------------------------------------
}





