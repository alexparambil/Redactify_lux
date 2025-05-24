import React, { useState } from "react";
import { Container, Typography, Button, Box } from "@mui/material";
import FileDropzone from "./components/FileDropzone";
import OutputDisplay from "./components/OutputDisplay";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);

    const handleSubmit = async () => {
    if (!file) return alert("Please select a PDF.");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("output_format", "both"); // "text", "pdf", or "both"

    try {
      const response = await axios.post("http://localhost:8000/process/", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });

      console.log(response.data);
      setResponse(response.data); // <- this matches your frontend state

    } catch (error) {
      console.error("Processing failed:", error);
    }
  };

  return (
    <Container maxWidth="md">
      <Typography variant="h4" sx={{ mt: 4, mb: 1 }}>🔐 Redactify Lux</Typography>
      <Typography variant="subtitle1" sx={{ mb: 3 }}>Illuminate Your Privacy</Typography>

      <FileDropzone onFileSelect={setFile} />

      <Button
        variant="contained"
        color="primary"
        sx={{ mt: 2 }}
        onClick={handleSubmit}
        disabled={!file}
      >
        Submit PDF
      </Button>

      {response && (
        <Box sx={{ mt: 4 }}>
          <OutputDisplay data={response} />
        </Box>
      )}
    </Container>
  );
}

export default App;
