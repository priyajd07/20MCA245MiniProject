import java.io.* ;
import java.net.*;

public class GpServer
  {
   public static void main(String args[]) throws Exception 
     {    
      int clientNumber=0,SelfPort=0;   

      if ( args.length > 0 )
         SelfPort = Integer.parseInt(args[0]);
      else
         SelfPort = 6801;

      ServerSocket welcomeSocket = new ServerSocket(SelfPort);
      System.out.println("JItecMw Listening on port "+ Integer.toString(SelfPort));
      
      while(true) 
         {
          try
	         {
	          new Middle(welcomeSocket.accept(), clientNumber++).start();
	      }
	      finally
             {
	          System.out.println("");
		  }  
       }
        
    }
// CD \Development\Student Projects\graphic_password

//------------------------------------------------------------------------------ 
  private static class Middle extends Thread 
    {
     private Socket connectionSocket;
     private int myNumber;
     public byte[][] DotStore = new byte[80][8]; //  dot pattern of characters stored as 8 bytes 8*8 = 64 docts fro

     public Middle(Socket socket, int clNumber) 
       {
        this.connectionSocket = socket;
        this.myNumber         = clNumber;
        System.out.println("Constructor " + clNumber + " at " + socket);
       }
 //-----------------run---------------------------------------------------------
   public  void run()
     { 
     
    String Str=""; boolean ex = false;
    
    while ( true ) 
    { 
    try 
      { 
       String First , Second ,UserId="";
       byte Password[] = 	new byte[ (int) 1024];
                        
       DataOutputStream ackout;
       byte[] Received = new byte[(int) 1024];
       boolean True    = false; 
       int Bcnt=0;

System.out.println("New connection with client# " + myNumber + " at " + connectionSocket);
       
       // for asccii communication
       ackout = new DataOutputStream(connectionSocket.getOutputStream());
      
       //for byte communication;
       BufferedInputStream  Breqin  = new BufferedInputStream(connectionSocket.getInputStream());

       Bcnt = From_Client(Breqin , Received);
       To_Client(ackout,"GO");

       //----First Program call-----------
       while(true) 
         {
           Bcnt = From_Client( Breqin , Received) ;                   
           Str  = bytesToString( Received , 2);
           First  = Str.substring(0,1);
           Second = Str.substring(1,2);
                                
          /*Packetes coming from client 
            First letter - Login , Regiatrtion
            Second I(d)  or password */

           if ( Second.equals("I")) 
             { 
               Str    = bytesToString( Received , Bcnt);
               UserId = Str.substring(2,Bcnt);
             
               True   = OpenId (UserId);


               if (UserId.length() < 5) 
                  // close the file
                  To_Client(ackout,"* ID should be atleast 5 characters");
               else 
               {            
                  if (First.equals("R")) 
                  {
                     if ( True )
                        To_Client(ackout,"* ID already exists");
                     else
                        To_Client(ackout,"OK");

                  }   
                  else if (First.equals("L")) 
                  {
                     if ( True ) 
                        To_Client(ackout,"OK");
  
                     else
                        To_Client(ackout,"* Wrong ID");
                  }     
               }        
            }
           else if (Second.equals("P"))
           {

               Password = Make_Straight(Received,Bcnt);
           	   
               if (First.equals("R")) 
               {
                 if ( Bcnt <= 2 ) 
                    To_Client(ackout,"Cannot create ID without password");                  
                 else {     
                    True = Create_And_Write(UserId,Password, (Bcnt-2)/2 );
                    
                    To_Client(ackout,"ID:" + UserId + " Created");
                      

                   }    
               }   
               else if (First.equals("L")) 
               {
               	 
                 True = Validate(UserId,Password,(Bcnt-2)/2);  
                 
                 if ( True )
                    To_Client(ackout,"Login Successful");
                 else
                    To_Client(ackout,"*Login Failed");

               } 
          }
        }  
      }    
    catch (IOException e) 
      {
       
       String Err =e.getMessage().toString();
       Err=String.format(Err).replace('\n','0');
       Str= "OE0"+String.format("%3s",Err.length()).replace(' ','0')+Err+"012From JItecMw      OK";
      }
    catch (Exception e) 
     {
       String Err =e.getMessage().toString();
       Err=String.format(Err).replace('\n','0');
       Str= "OE0"+String.format("%3s",Err.length()).replace(' ','0')+Err+"012From JItecMw      OK";
       
     }
            
     break;
   }
 } 
 //---------------------Receives data from clint as bytes--------------------------------
  private int From_Client(BufferedInputStream R , byte[] Get) 
  {
  	int Cnt=0;
  	
  	try {
       while ( (Cnt = R.read(Get)) == 0);
 System.out.print("From cl :" + Cnt );

       if ( Cnt < 15 ) 
System.out.println(" " + bytesToString(Get, Cnt));
       else
System.out.println(" ");

    }   
    catch ( IOException e)
      {}
    return Cnt; 
  }
 //-------------------------Send data to client as characters -----------------------
  private void To_Client(DataOutputStream S, String Snd) 
  {
    try {
  	    S.writeBytes(Snd +'\n' );
        S.flush();
  	    System.out.println("To client:" + Snd);
    }
    catch ( Exception e)
    {            System.out.println(e.toString() + "problem Sending to client  "+ Snd);
    }     
  }
 //-------Converts bytes in buffr to string to get userid ----------------------------------------
  private String bytesToString(byte[] bytes, int Cnt) {
   char[] buffer = new char[Cnt];
   
   for(int i = 0; i < buffer.length; i++) {
       int bpos = i << 1;
       char c = (char)( 0000 | bytes[i]);
       buffer[i] = c;
   }
   
   return new String(buffer);
  }
  // -----------------------------------------------String to byte----------------------------------------------------
  private  byte[] stringToBytes(String str) {
   char[] buffer = str.toCharArray();
   byte[] b = new byte[buffer.length];
   
   int Bcnt = buffer.length;
   
   for (int i = 0; i < b.length; i++) {
      b[i] = (byte) (buffer[i]&0x00FF);
     
   }
   return b;
}

 //---------- Opn file and connect to stream-----------------------------------------------------
  private boolean OpenId (String Nam) 
  {
      File Fil;
      BufferedInputStream Bf = null;
      boolean Opened;
      
      try
      {
        Fil = new File(Nam);
        Bf = new BufferedInputStream(new FileInputStream(Fil));
        Opened = true;
        
        Bf.close();
                
      } catch (IOException e)
      {
         Opened = false;        
        
      }
      
      return Opened;
   }
 //----------  Read file-------------------------------------------------------------------------
  private boolean Create_And_Write (String Nam , byte[] Password, int Ln) 
   {
      File Fil;
      BufferedOutputStream Bfo = null;
      boolean Sucess = false;
      int Bcnt=0;
      String PassPlus;

      Fil = new File(Nam);
       
      try 
	   	{
    	  Fil.createNewFile();
          Sucess = true; 
		}
      catch (Exception e) 
        {
         Sucess = false; 
         System.out.println("Saving: text file creation error");
      } 			    

System.out.println( Password.length + " " + Ln ); 

      if ( Sucess ) {
         try
            {
             Bfo = new BufferedOutputStream(new FileOutputStream(Fil));
             Bfo.write(Password , 0 , Ln );
             Bfo.flush();
             Bfo.close();
             Sucess = true;
          }
         catch ( Exception e)
          {
            System.out.println("File writing error ");
            Sucess = false;
         }
      }
            
      return Sucess;
   }
 //----------  Read file-------------------------------------------------------------------------
  private byte[] Make_Straight(byte[] Rec , int Ln ) 
   {        
      int  NoOfCh = (Ln-2)/16, off=0;
      
      byte [] Pw = new byte[NoOfCh*8];
      byte Rst= 0 ,Dat1 = 0 , Dat2 = 0, Tst1 = 0 , Tst2=0;
   try {
            
              
      for ( int ch=0 ; ch < NoOfCh ; ch++)
   	   {
         for ( int j = 0 ; j < 16 ; j=j+2)
         {
           Rst = Rec[ch*16+j+2];
        
           //Separate the First byte   into Nibble Tstm and  Datm  
           Dat1 = (byte)  (Rst & 0x0F);
           Tst1 = (byte)   (Rst & 0xF0);
         
           Rst = Rec[ch*16+j+2+1];

           //Separate the Least Sig byte of (2)  into Nibble Tstl and  Datl  
           Dat2 = (byte)  (Rst & 0x0F);
           Tst2 = (byte)   (Rst & 0xF0);
 
           if (  Tst1 < 0 )  // negative quantity represnts Most significant nibble of the raster
               //Store Lsb first and then MSb with offset based on offset and Boffset
            {
              Rst = (byte) (Dat1 << 4 | Dat2);               
              off = (int) Tst2/16;
            }
           else
            {
              Rst = (byte) (Dat2 << 4 | Dat1);               
              off = (int) Tst1/16;
           }

           Pw[ch*8 + off]   = Rst;           
      }
    } 

   } 
catch ( Exception e) {
        System.out.println ( "eERROR " + e );         
   }

   return Pw;
}
 

 //----------  Read file-------------------------------------------------------------------------
  private boolean Validate (String Nam , byte[] Rec , int Ln ) 
   {
      File Fil;
      BufferedInputStream Bf = null;
      boolean Success;
      byte[] RdBuff = new byte[1024];
      int Bcnt=0, Plen=0;
              
      try
      {
        Fil = new File(Nam);
        Bf = new BufferedInputStream(new FileInputStream(Fil));
        Success = true;

        Bcnt = Bf.read(RdBuff , 0 , 1024);
        
        Bf.close();          
      } 
      catch (IOException e)
      {
        Success = false;        
        e.printStackTrace();
        return Success;
      }
                 
      Success = true;

      if ( Bcnt != Ln ) 
         Success = false;

      else      {
         for ( int ii=0 ; ii < Bcnt ; ii++)
         {

           try {
              if ( RdBuff[ii] != Rec[ii]) {
              Success = false;
              break;
           }
         }  
          catch ( Exception e) {
            Success = false;
            break;
          }      
        }
     }
      return Success;
   }
  }
} 