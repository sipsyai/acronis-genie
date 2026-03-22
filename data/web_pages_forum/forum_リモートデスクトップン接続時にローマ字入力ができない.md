# リモートデスクトップン接続時にローマ字入力ができない

**Forum:** Acronis Cyber Protect Cloud Forum
**URL:** https://forum.acronis.com/forum/acronis-cyber-protect-cloud-forum/rimototesukutotsufunjiexushiniromazirulikatekinai

## Original Post
**Author:** Unknown

リモートデスクトップン接続時にローマ字入力ができない

        
  



    
  


  
          
  
    Tutorial
  


          






    
        

            
                
                    
    
        
            
                
              



      
            
        
        
            
                                    tanaka tsutomu
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 2
                
            
            
                
                    Comments: 0
                
            
                                                        
    
    
        
    


                
                
                    
                        
            クラウドコンソールから遠隔でリモートデスクトップ接続「NEAR」「RDP」とも接続先のWindows11パソコン上でローマ字入力ができません。
キーボードの設定も試しましたがNGでした
サポートの問い合わせでは明確な回答をもらえませんでした。
※そもそも簡単な操作しかリモートでは想定していないとか・・・言われました
 
成功した事例あれば大変助かります。

      
                                            
                
            
                            
                    
                        
                            
                              Sat, 12/13/2025 - 06:46

                                                          
                                                            
                                                                                
                    
                
                        
            
                
  
  



    
    


  
  0 Users found this helpful



                
  
  





            
                    
    

            
  
  

    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    José P. M.
                            

                            
                    
                        Community Owner
                    
                
            
                        
                
                    Posts: 34
                
            
            
                
                    Comments: 4480
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            こんにちは、
ご報告ありがとうございます。
クラウドコンソール経由でのリモートデスクトップ接続（NEAR/RDP）でローマ字入力ができない問題については、残念ながら 現状サポート対象外のケース である可能性があります。特に Windows 11 環境では、リモート接続時の入力方式や IME の動作に制限がある場合があります。
いくつか試せることとしては：

接続先のWindowsでIMEを英字（ローマ字）モードに固定


RDPのローカルリソース設定でキーボードを適切にマッピング


別のリモートクライアントやブラウザからの接続を試す

ただし、クラウドコンソール経由でのリモート操作は 簡単な操作を想定しており、フルIME入力や複雑な日本語入力はサポートされない場合があります。
もし、英字入力を安定して行いたい場合は、ローカルRDPクライアントから直接接続する方法が最も確実です。
同様の事例で成功した方がいれば、ぜひ共有していただけると助かります。

      
                
                
                    
                                                    Wed, 01/07/2026 - 22:47
                                                                            
                                
                            
                                            
                                            
    
                    
                Best regards,
Jose P. M. | Community Owner

Information provided AS-IS with no warranty of any kind.

To contact support, please follow http://www.acronis.com/en-us/support

            
                    
                                                                            
            
        
    



    
        
        
            
                
    
        
            
                
              



      
            
        
        
            
                                    Elena Ermurt
                            

                            
                    
                        Beginner
                    
                
            
                        
                
                    Posts: 0
                
            
            
                
                    Comments: 1
                
            
                                                        
    
    
        
    


                
                    
                
            
            
                
                    
                
                
                    
                        
                    
                    
            この症状、RDPでは意外とよくあります。多くの場合、原因は「入力方式の引き継ぎ」と「IMEの動作場所」にあります。まず確認したいのは、RDP接続後に接続先のWindows 11側でIMEが本当に有効になっているかどうかです。タスクバーにIMEアイコンが表示されていても、直接日本語IMEに切り替え直す必要があるケースがあります。また、RDPクライアント側のキーボード設定で「ローカルのキーボードを使用」になっているかも重要です。成功事例では、Microsoft IMEを一度削除して再追加、または英語キーボードを一時的に無効化することで改善した例もあります。NEARや独自コンソール経由の場合、そもそもIME非対応な実装もあるため、通常のmstsc.exe経由でのRDP接続も一度試す価値があります。

      
                
                
                    
                                                    Sat, 01/17/2026 - 07:22
