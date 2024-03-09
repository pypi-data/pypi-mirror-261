import React, { useRef, useState } from "react";
import Sidebar from "../components/Sidebar";
import { BiMinus } from "react-icons/bi";
import {
  FiMenu,
  FiPlus,
  FiSearch,
  FiXCircle,
} from "react-icons/fi";

import ChatBotSideBar from "../components/chatBot/ChatBotSideBar";
import { Chat } from "../components/chatBot/Chat";


const ChatBot = () => {
  const uploadedFiles = [
    {
      lastModified: "2024-03-04, 10:30",
      name: "document1.pdf",
      type: "pdf",
      file: "path/to/document1.pdf",
      key: "unique_key_1",
    },
    {
      lastModified: "2024-03-04, 10:30",
      name: "image1.docs",
      type: "docs",
      file: "path/to/image1.docs",
      key: "unique_key_2",
    },
    {
      lastModified: "2024-03-04, 10:30",
      name: "spreadsheet1.text",
      type: "text",
      file: "path/to/spreadsheet1.text",
      key: "unique_key_3",
    },
    {
      lastModified: "2024-03-04, 10:30",
      name: "document1.pdf",
      type: "pdf",
      file: "path/to/document1.pdf",
      key: "unique_key_1",
    },
    {
      lastModified: "2024-03-04, 10:30",
      name: "image1.docs",
      type: "docs",
      file: "path/to/image1.docs",
      key: "unique_key_2",
    },
    {
      lastModified: "2024-03-04, 10:30",
      name: "spreadsheet1.text",
      type: "text",
      file: "path/to/spreadsheet1.text",
      key: "unique_key_3",
    },
  ];

  const [isCollections, setIsCollections] = useState(true);

  return (
    <div className="flex">
      <div className="w-1/5 font-cerebri flex border-r-[0.5px] border-[#CDCDCD]">
        <Sidebar />
        <ChatBotSideBar uploadedFiles={uploadedFiles} setIsCollections={setIsCollections} isCollections={isCollections}/>
     
      
      </div>
      <div className="col-span-6 h-screen w-4/5">
          <div className="grid grid-cols-2">
            <div className="col-span-1">
              {
                isCollections ? "" :  <div className="flex items-center justify-between py-[19px] px-3 border-b border-[#E8E9EA]">
                <div className="flex items-center gap-4">
                  {/* <FiMenu className="text-[20px] text-[#9B9EA3]" /> */}

                  {/* {numPages && pageNumber && ( */}
                  <div className="text-[#1C232D] font-cerebri font-normal text-[16px]">
                    <span className="bg-[#F2F4FE] px-3 py-1 rounded-lg">1</span>{" "}
                    / 4
                  </div>
                  {/* )} */}
                </div>

                <div className="flex items-center gap-3">
                  <FiPlus
                    className="text-[18px] cursor-pointer"
                    //  onClick={increaseResolution}
                  />
                  <div className="text-[#1C232D] text-[16px] font-cerebri font-normal bg-[#F2F4FE] rounded py-1/2 px-1">
                    {/* {displayPercentage}% */}
                    100%
                  </div>
                  <BiMinus
                    className="text-[18px] cursor-pointer"
                    // onClick={decreaseResolution}
                  />
                </div>

                <div className="flex items-center gap-2 relative">
                  {/* {isSearchVisible && ( */}
                  <input
                    type="text"
                    className="border border-[#EEEFEF] py-[3px] -mt-1 -mb-1 px-4 rounded-lg outline-none text-[#808DA4] text-[16px] font-cerebriregular font-normal"
                    placeholder="search"
                    // value={searchText}
                    // onChange={(e) => setSearchText(e.target.value)}
                  />
                  {/* // )} */}

                  {/* {searchText && isSearchVisible && ( */}
                  <span
                    className="absolute text-blackText right-8 top-1/2 transform -translate-y-1/2 cursor-pointer"
                    // onClick={() => setSearchText("")}
                  >
                    <FiXCircle className="text-[#A4A7AB] text-[20px]" />
                  </span>
                  {/* )} */}

                  <FiSearch
                    className="text-[#A4A7AB] text-[20px] cursor-pointer"
                    //   onClick={() => setIsSearchVisible(!isSearchVisible)}
                  />
                </div>
              </div>
              }
            

              <div className={`bg-[#F3F4F6] ${isCollections ? "100vh" :"h-[calc(100vh-65px)]" } ps-7 pe-7 pt-1`}>
              {/* h-[calc(100vh-52px)] */}
                <div className="chatscreen  overflow-auto">
                  {/* {selectedFileContent && (
                  <>
                    {typeof fileType === "string" && fileType.startsWith("text") ? (
                      <div className="flex justify-center w-fit mt-5 break-words">
                        <div
                          className="text-[#00102D] font-medium text-[16px] font-cerebri bg-white py-14 px-16 rounded-lg max-w-3xl"
                          style={{ fontSize: `${displayPercentage}%` }}
                        >
                          {highlightText(selectedFileContent, searchText)}
                        </div>
                      </div>
                    ) : fileType ===
                      "application/vnd.openxmlformats-officedocument.wordprocessingml.document" ? (
                      <DocumentViewer queryParams="hl=Nl" url={fileUrl} />
                    ) : fileType === "" ? (
                      <DocumentViewer queryParams="hl=Nl" url={fileUrl} />
                    ) : (
                      <Worker workerUrl={`https://unpkg.com/pdfjs-dist@3.11.174/build/pdf.worker.min.js`}>
                        <Viewer
                          fileUrl={fileUrl}
                          plugins={plugins}
                          onPageChange={handlePageChange}
                          defaultScale={1.5}
                        />
                      </Worker>
                    )}
                  </>
                )} */}
                </div>
              </div>
            </div>

            <div className="col-span-1 border-l border-[#E8E9EA]">
            <Chat/>
            </div>
          </div>
        </div>
    </div>
  );
};

export default ChatBot;
