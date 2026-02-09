import React, { useState } from 'react';
import './App.css';

const API_URL = 'http://127.0.0.1:8000';

function App() {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState('');
  const [correctedText, setCorrectedText] = useState('');
  const [rawText, setRawText] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [status, setStatus] = useState('');
  const [llmStatus, setLlmStatus] = useState(null);
  const [usedLlm, setUsedLlm] = useState(false);
  const [showAbout, setShowAbout] = useState(false);

  // Check LLM status on component mount
  React.useEffect(() => {
    checkLlmStatus();
  }, []);

  const checkLlmStatus = async () => {
    try {
      const response = await fetch(`${API_URL}/status`);
      const data = await response.json();
      setLlmStatus(data);
    } catch (err) {
      console.error('Failed to check LLM status:', err);
    }
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setFileName(selectedFile.name);
      setCorrectedText('');
      setRawText('');
      setError('');
      setStatus('');
      setUsedLlm(false);
    }
  };

  const handleProcess = async () => {
    if (!file) {
      setError('Please select a file first');
      return;
    }

    setLoading(true);
    setError('');
    setCorrectedText('');
    setRawText('');
    setStatus('Файл бэлтгэж байна...');
    setUsedLlm(false);

    try {
      const formData = new FormData();
      formData.append('file', file);

      setStatus('OCR таниж байна...');
      
      const response = await fetch(`${API_URL}/process`, {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Processing failed');
      }

      if (data.success) {
        setRawText(data.raw_text || '');
        setCorrectedText(data.corrected_text || '');
        setUsedLlm(data.used_llm || false);
        
        if (data.used_llm) {
          setStatus('Моделоор засуулж дууслаа!');
        } else {
          setStatus('Энгийн цэвэрлэлт хийж дууслаа!');
        }
        
        // Clear status after 3 seconds
        setTimeout(() => setStatus(''), 3000);
      } else {
        setError(data.error || 'Processing failed');
        setStatus('');
      }
    } catch (err) {
      setError(err.message || 'Failed to process document');
      setStatus('');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleExport = async () => {
    if (!correctedText) {
      setError('No corrected text to export');
      return;
    }

    try {
      const response = await fetch(`${API_URL}/export`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: correctedText }),
      });

      if (!response.ok) {
        throw new Error('Export failed');
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'corrected_text.docx';
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    } catch (err) {
      setError(err.message || 'Failed to export document');
      console.error('Error:', err);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="header-content">
          <div>
            <h1>PDF to Word</h1>
            <p className="subtitle">Монгол бичвэрийн OCR ба засвар</p>
          </div>
          <button 
            className="about-button"
            onClick={() => setShowAbout(true)}
            title="Аппын тухай"
          >
            ℹ️ Аппын тухай
          </button>
        </div>
      </header>

      <main className="App-main">
        {/* LLM Status Indicator */}
        {llmStatus && (
          <div className={`status-indicator ${llmStatus.llm_ready ? 'status-ready' : 'status-simple'}`}>
            {llmStatus.llm_ready ? (
              <span>✅ LLM загвар бэлэн байна</span>
            ) : (
              <span>ℹ️ Энгийн текст цэвэрлэлт ашиглана</span>
            )}
          </div>
        )}

        <div className="upload-section">
          <div className="file-input-wrapper">
            <input
              type="file"
              id="file-input"
              accept=".pdf,.png,.jpg,.jpeg"
              onChange={handleFileChange}
              className="file-input"
            />
            <label htmlFor="file-input" className="file-label">
              {fileName || 'Файл сонгох (PDF, PNG, JPG)'}
            </label>
          </div>

          <button
            onClick={handleProcess}
            disabled={!file || loading}
            className="process-button"
          >
            {loading ? (status || 'Боловсруулж байна...') : 'OCR + Засах'}
          </button>
        </div>

        {/* Process Status */}
        {status && (
          <div className="process-status">
            <div className="status-message">
              {status}
            </div>
            {loading && (
              <div className="status-steps">
                {status.includes('OCR') && (
                  <>
                    <div className="step active">1. OCR таниж байна...</div>
                    <div className="step">2. Текст засуулж байна...</div>
                  </>
                )}
                {(status.includes('Моделоор') || status.includes('Энгийн')) && (
                  <>
                    <div className="step completed">1. OCR таниж дууслаа ✓</div>
                    <div className="step active">2. {status.includes('Моделоор') ? 'Моделоор засуулж байна...' : 'Энгийн цэвэрлэлт хийж байна...'}</div>
                  </>
                )}
              </div>
            )}
          </div>
        )}

        {/* LLM Usage Indicator */}
        {correctedText && usedLlm && (
          <div className="llm-used-indicator">
            ✅ LLM загварыг ашиглан зассан
          </div>
        )}
        {correctedText && !usedLlm && (
          <div className="simple-used-indicator">
            ℹ️ Энгийн текст цэвэрлэлт ашигласан
          </div>
        )}

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {correctedText && (
          <div className="text-preview-section">
            <div className="preview-header">
              <h2>Зассан бичвэр</h2>
              <button
                onClick={handleExport}
                className="export-button"
              >
                Word-д татах
              </button>
            </div>
            <div className="text-preview">
              <pre>{correctedText}</pre>
            </div>
          </div>
        )}

        {rawText && correctedText !== rawText && (
          <div className="text-preview-section">
            <div className="preview-header">
              <h3>Анхны OCR текст</h3>
            </div>
            <div className="text-preview raw-text">
              <pre>{rawText}</pre>
            </div>
          </div>
        )}
      </main>

      {/* About Modal */}
      {showAbout && (
        <div className="modal-overlay" onClick={() => setShowAbout(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <h2>PDF to Word</h2>
              <button className="modal-close" onClick={() => setShowAbout(false)}>×</button>
            </div>
            <div className="modal-body">
              <div className="about-section">
                <h3>Хувилбар</h3>
                <p>V1.0</p>
              </div>

              <div className="about-section">
                <h3>Ашигласан технологи</h3>
                <ul>
                  <li><strong>Frontend:</strong> Electron + React</li>
                  <li><strong>Backend:</strong> Python + FastAPI</li>
                  <li><strong>OCR:</strong> Tesseract OCR (Монгол + Англи хэл)</li>
                  <li><strong>Зураг боловсруулалт:</strong> OpenCV</li>
                  <li><strong>AI засвар:</strong> llama.cpp (Offline LLM)</li>
                  <li><strong>PDF боловсруулалт:</strong> Poppler, PyPDF2</li>
                  <li><strong>Экспорт:</strong> python-docx (Word баримт бичиг)</li>
                </ul>
              </div>

              <div className="about-section">
                <h3>Онцлогууд</h3>
                <ul>
                  <li>✅ PDF болон зураг (PNG, JPG) дэмжих</li>
                  <li>✅ Монгол кирилл үсгийн OCR</li>
                  <li>✅ LLM модел ашиглан OCR-ийн алдааг автоматаар засах</li>
                  <li>✅ Албан ёсны оффис хэлбэрт шилжүүлэх</li>
                  <li>✅ Бүх боловсруулалт офлайн (интернет шаардлагагүй)</li>
                  <li>✅ Word баримт бичиг (.docx) экспортлох</li>
                </ul>
              </div>

              <div className="about-section">
                <h3>LLM Загвар</h3>
                <p>
                  Энэ апп нь LLM (Large Language Model) загварыг ашиглан OCR-ийн алдааг 
                  автоматаар засах, албан ёсны оффис хэлбэрт шилжүүлэх боломжтой. 
                  LLM загвар байхгүй тохиолдолд энгийн текст цэвэрлэлт хийх болно.
                </p>
              </div>

              <div className="about-section">
                <h3>Нэмэлт хөгжүүлэлт</h3>
                <p>
                  Хэрэв танд нэмэлт функц, онцлог нэмэх хэрэгтэй бол бидэнтэй холбогдоно уу. 
                  Бид таны хэрэгцээнд тохирсон хөгжүүлэлт хийх боломжтой.
                </p>
              </div>

              <div className="about-section">
                <h3>Холбоо барих</h3>
                <p>
                  <strong>Viber:</strong> <a href="viber://chat?number=88076625" className="contact-link">88076625</a>
                </p>
              </div>

              <div className="about-footer">
                <p>© 2024 PDF to Word. Бүх эрх хуулиар хамгаалагдсан.</p>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
