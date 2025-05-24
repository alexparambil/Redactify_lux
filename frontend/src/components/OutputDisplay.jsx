import React from "react";
import { Box, Typography, Divider } from "@mui/material";

function OutputDisplay({ data }) {
  return (
    <Box mt={4} maxWidth="1200px" mx="auto">
      {/* Display Classification */}
      <Typography variant="h5" sx={{ mb: 3, fontWeight: "bold" }}>
        Classification: {data.classification}
      </Typography>

      <Typography variant="h6" mb={2}>Extracted vs Redacted Text:</Typography>
      <Box sx={{ display: "flex", gap: 4, justifyContent: "center", alignItems: "flex-start" }}>
        {/* Extracted Text Box */}
        <Box
          sx={{
            width: "48%",
            backgroundColor: "#f5f5f5",
            borderRadius: 1,
            boxShadow: "0 0 10px rgba(0,0,0,0.1)",
            display: "flex",
            flexDirection: "column",
            maxHeight: 500,
            overflowY: "auto",
            position: "relative",
          }}
        >
          <Typography
            variant="subtitle1"
            sx={{
              position: "sticky",
              top: 0,
              backgroundColor: "#f5f5f5",
              zIndex: 1,
              p: 1,
              borderBottom: "1px solid #ccc",
              fontWeight: "bold",
            }}
          >
            Extracted Text:
          </Typography>
          <Box sx={{ whiteSpace: "pre-wrap", p: 2, wordBreak: "break-word" }}>
            {data.extracted_text}
          </Box>
        </Box>

        {/* Redacted Text Box */}
        <Box
          sx={{
            width: "48%",
            backgroundColor: "#f0e6e6",
            borderRadius: 1,
            boxShadow: "0 0 10px rgba(0,0,0,0.1)",
            display: "flex",
            flexDirection: "column",
            maxHeight: 500,
            overflowY: "auto",
            position: "relative",
          }}
        >
          <Typography
            variant="subtitle1"
            sx={{
              position: "sticky",
              top: 0,
              backgroundColor: "#f0e6e6",
              zIndex: 1,
              p: 1,
              borderBottom: "1px solid #ccc",
              fontWeight: "bold",
            }}
          >
            Redacted Text:
          </Typography>
          <Box sx={{ whiteSpace: "pre-wrap", p: 2, wordBreak: "break-word" }}>
            {data.redacted_text}
          </Box>
        </Box>
      </Box>

      <Divider sx={{ my: 3 }} />

      {/* PDFs side by side */}
      <Typography variant="h6" mb={2}>Original vs Redacted PDF:</Typography>
      <Box sx={{ display: "flex", gap: 4, justifyContent: "center" }}>
        <Box sx={{ width: "48%", height: 600, border: "1px solid #ccc", borderRadius: 1 }}>
          <Typography
            variant="subtitle1"
            sx={{
              backgroundColor: "#fff",
              p: 1,
              fontWeight: "bold",
              borderBottom: "1px solid #ccc",
            }}
          >
            Original PDF
          </Typography>
          <iframe
            title="Original PDF"
            src={`data:application/pdf;base64,${data.original_pdf_base64}`}
            style={{ width: "100%", height: "calc(100% - 40px)", border: "none" }}
          />
        </Box>

        <Box sx={{ width: "48%", height: 600, border: "1px solid #ccc", borderRadius: 1 }}>
          <Typography
            variant="subtitle1"
            sx={{
              backgroundColor: "#fff",
              p: 1,
              fontWeight: "bold",
              borderBottom: "1px solid #ccc",
            }}
          >
            Redacted PDF
          </Typography>
          <iframe
            title="Redacted PDF"
            src={`data:application/pdf;base64,${data.redacted_pdf_base64}`}
            style={{ width: "100%", height: "calc(100% - 40px)", border: "none" }}
          />
        </Box>
      </Box>

      <Divider sx={{ my: 3 }} />

      <Typography variant="h6">Download Files:</Typography>
      <a href={`data:application/pdf;base64,${data.original_pdf_base64}`} download="original.pdf">
        ⬇️ Download Original
      </a>
      <br />
      <a href={`data:application/pdf;base64,${data.redacted_pdf_base64}`} download="redacted.pdf">
        ⬇️ Download Redacted
      </a>
    </Box>
  );
}

export default OutputDisplay;
