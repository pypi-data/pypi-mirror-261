import React, { useState } from "react";
import { AiOutlinePlusCircle } from "react-icons/ai";
import { MdDelete } from "react-icons/md";
import { FaChevronLeft } from "react-icons/fa";
import pdfIcon from "../../assets/pdf.svg";
import textIcon from "../../assets/text.svg";
import docxIcon from "../../assets/docs.svg";
import odtIcon from "../../assets/odt.png";
import wave from "../../images/wave.png";
import dots from "../../images/dots.png";
import folder from "../../assets/folder.svg";
import arrowLeft from "../../assets/arrowLeft.svg";



const ChatBotSideBar = ({ uploadedFiles = [],setIsCollections,isCollections }) => {
  const collections = ["abc","xyz","dots","dolor","large text","test folder"];
  const getFileIcon = (fileType) => {
    if (fileType.includes("pdf")) {
      return pdfIcon;
    } else if (fileType.includes("doc")) {
      return docxIcon;
    } else if (fileType.includes("text")) {
      return textIcon;
    } else {
      return odtIcon;
    }
  };
  
  return (
    <div className="col-span-1 w-[100%]">
      <div className="flex items-center justify-between px-4 py-4 border-b ">
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-3">
            <img src={wave} alt="" className="w-[30px] h-[30px]" />
            <h1 className="text-blackText font-cerebri text-[21px] leading-[27px]">
              AI assistant
            </h1>
          </div>
        </div>
      </div>
      {isCollections ? (
        <>
          {" "}
          <div className="flex items-center justify-between pt-4 px-5">
            <div className="text-blackText  text-[16px] font-cerebriMedium">
              Collections
            </div>
          </div>
          <div>
            <div className="sidebar h-[calc(100vh-156px)] overflow-auto">
              {collections.map((item, index) => {
                return (
                  <div
                    className={`flex items-center justify-between px-3 py-2 mt-1 cursor-pointer overflow-hidden`}
                  >
                    <div key={index} className={`flex items-center gap-2 cursor-pointer`} onClick={()=>setIsCollections(false)}>
                     <span className="bg-customsky p-2 rounded-[5px]">
                     <img src={folder} className="w-5 h-5" alt="" />
                     </span>

                     
                      <div>
                        <div className="text-blackText font-medium font-cerebri text-[14px] w-[110px] whitespace-nowrap overflow-hidden text-ellipsis">
                          {item}
                        </div>
                      </div>
                    </div>
                    <img src={dots} alt="dots" className="min-w-[16px]" />
                  </div>
                );
              })}
            </div>
            <div className="mx-3">
              <div className="flex items-center gap-2 py-3">
                <AiOutlinePlusCircle className="text-blackText text-[20px]" />
                <div className="text-blackText font-normal font-cerebri text-[14px]">
                  New collection
                </div>
              </div>
            </div>
          </div>
        </>
      ) : (
        <>
          {" "}
          <div className="py-3 px-5 flex flex-col gap-4 border-b border-customGray">
          <div className="text-blackText flex text-[16px] gap-1 font-cerebriMedium cursor-pointer " onClick={()=>setIsCollections(true)}>
            <img src={arrowLeft} className="w-5 h-5"/>
              Collection 
            </div>
            <span className="text-blackText  text-[16px] font-cerebriMedium">
              Files
            </span>
          </div>
          <div>
            <div className="sidebar h-[calc(100vh-204px)] overflow-auto">
              {uploadedFiles.map((file, index) => {
                return (
                  <div
                    className={`flex items-center justify-between px-3 py-2 mt-1 cursor-pointer overflow-hidden`}
                  >
                    <div key={index} className={`flex items-center gap-2`}>
                      <span className="bg-customsky p-2 rounded-[5px]">
                      <img src={getFileIcon(file.type)} alt="" className="w-5 h-5"/>
                      </span>

                     
                      <div>
                        <div className="text-blackText font-medium font-cerebri text-[14px] w-[110px] whitespace-nowrap overflow-hidden text-ellipsis">
                          {file.name}
                        </div>
                      </div>
                    </div>
                    <img src={dots} alt="dots" className="min-w-[16px]" />
                  </div>
                );
              })}
            </div>
            <div className="mx-3">
              <div className="flex items-center gap-2 py-3">
                <AiOutlinePlusCircle className="text-blackText text-[20px]" />
                <div className="text-blackText font-normal font-cerebri text-[14px]">
                  New document
                </div>
              </div>
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default ChatBotSideBar;
