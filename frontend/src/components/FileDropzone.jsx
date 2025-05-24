import React, { useState } from "react";
import { Box, Typography, Paper } from "@mui/material";

function FileDropzone({ onFileSelect }) {
  const [isDragging, setIsDragging] = useState(false);
  const [fileName, setFileName] = useState("");

  const handleChange = (e) => {
    const file = e.target.files[0];
    if (file && file.type === "application/pdf") {
      setFileName(file.name);
      onFileSelect(file);
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);

    const file = e.dataTransfer.files[0];
    if (file && file.type === "application/pdf") {
      setFileName(file.name);
      onFileSelect(file);
    }
  };

  return (
    <Paper
      elevation={3}
      sx={{
        p: 4,
        textAlign: "center",
        cursor: "pointer",
        border: isDragging ? "2px solid #1976d2" : "1px dashed gray",
        backgroundColor: isDragging ? "#e3f2fd" : "inherit",
      }}
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
    >
      <Typography variant="body1">Drag or click to upload PDF</Typography>

      <input
        type="file"
        accept="application/pdf"
        onChange={handleChange}
        hidden
        id="pdf-upload"
      />

      <label htmlFor="pdf-upload">
        <Box
          component="span"
          sx={{
            display: "inline-block",
            mt: 2,
            p: 1,
            border: "1px dashed gray",
            borderRadius: 1,
          }}
        >
          📄 Choose PDF
        </Box>
      </label>

      {fileName && (
        <Typography variant="subtitle2" sx={{ mt: 2, color: "green" }}>
          Selected file: {fileName}
        </Typography>
      )}
    </Paper>
  );
}

export default FileDropzone;
