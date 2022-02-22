
class  CharMain
  {              
//-----------------------------------------------------------------------
   public  static void main(String argv[]) throws Exception
     {     	
       CharShape Clnt = new CharShape();

      try
        {   
           Clnt.Design();                           
       } 
      catch(Exception e)
        {
         System.out.println(e.toString()+"Error ");               
      }
   }
     
}

