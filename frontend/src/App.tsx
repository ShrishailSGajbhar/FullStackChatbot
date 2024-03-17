import React, { useState } from "react";
import { ChakraProvider, Box, Text, Input, Button, FormControl, FormLabel, FormErrorMessage, Center } from "@chakra-ui/react";

export default function App() {
  const [upload_result, setUploadResult] = useState();
  const [result, setResult] = useState();
  const [question, setQuestion] = useState("");
  const [file, setFile] = useState(null);
  const [userSelectedFile, setUserSelectedFile] = useState<string>("");
  const [sessionId, setSessionId] = useState('');

  const handleQuestionChange = (event: any) => {
    setQuestion(event.target.value);
  };

  const handleFileChange = (event: any) => {
    const file = event.target.files[0] as File; 
    setFile(event.target.files[0]);
    setUserSelectedFile(file.name);
    const formData = new FormData();
    const reader = new FileReader();
    reader.onload = (e) => {
      const fileContent = e?.target?.result;
      if (fileContent) {
        // Check if the type is ArrayBuffer
        if (fileContent instanceof ArrayBuffer) {
          // Convert ArrayBuffer to Blob
          const blob = new Blob([fileContent], { type: "application/octet-stream" });
          formData.append("file", blob, event.target.files[0].name);
        } else {
          // If it's already a string, use it directly
          formData.append("file", fileContent, event.target.files[0].name);
        }
        fetch("http://127.0.0.1:8000/upload_process_file", {
          method: "POST",
          body: formData,
        })
          .then((response) => response.json())
          .then((data) => {
            setUploadResult(data.result);
  
            // Build the user_selected_files list
            const url = `http://127.0.0.1:8000/prepare_chatbot?uploaded_filepath=${file.name}`;
            fetch(url, {
              method: "POST",
              headers: {
                "Content-Type": "application/json"
              },
            })
              .then((response) => response.json())
              .then((data) => {
                console.log("Chatbot prepared:", data);
                // Store the session_id for later use
                setSessionId(data.session_id);
                // Handle successful chatbot preparation (e.g., enable chat functionality)
              })
              .catch((error) => {
                console.error("Error in prepare_chatbot call:", error);
                // Handle specific errors (e.g., display user-friendly messages)
              });
          })
          .catch((error) => {
            console.error("Error in upload_process_file call:", error);
            // Handle upload errors (e.g., display error messages)
          });
      } else {
        console.error("Error reading file");
      }
    };
    reader.readAsArrayBuffer(event.target.files[0]);
  };
  

  const handleSubmit = (event: any) => {
    event.preventDefault();
    const formData = new FormData();
    if (file) {
      formData.append("file", file);
    }
    if (question) {
      formData.append("question", question);
    }
    const url = `http://127.0.0.1:8000/chat?query=${question}`;
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
    })
      .then((response) => response.json())
      .then((data) => {
        setResult(data.result);
      })
      .catch((error) => {
        console.error("Error", error);
      });
  };

  return (
    <ChakraProvider>
      <Box className="appBlock" textAlign="center" fontSize="xl">
        <Text fontWeight="bold">Chat with Your Document</Text>
        <form onSubmit={handleSubmit} className="form">
          <FormControl mt={4} isInvalid={!file}>
            <FormLabel htmlFor="file">Upload a CSV (required):</FormLabel>
            <Input type="file" id="file" name="file" accept=".csv,.txt,.docx,.pdf" onChange={handleFileChange} className="fileInput" /> {!file && <FormErrorMessage>Please select either a CSV, DOCX, TXT or PDF file.</FormErrorMessage>}
          </FormControl>
          {file && (
            <Center mt={4}>
              <Text color="green.500">File upload successful! Ask your question now!</Text>
            </Center>
          )}
          {file && (
            <FormControl mt={4}>
              <FormLabel htmlFor="question">Your Question:</FormLabel>
              <Input className="questionInput" id="question" type="text" value={question} onChange={handleQuestionChange} placeholder="Ask your question here..." />
            </FormControl>
          )}
          <br />
          {file && (
            <Button colorScheme="teal" type="submit" disabled={!question}>
              Ask Away!
            </Button>
          )}
        </form>
        
        <Text mt={4}>Answer:</Text>
        <Text as="p" className="resultOutput">{result}</Text>
      </Box>
    </ChakraProvider>
  );
}
