import React, { useEffect, useRef } from 'react';
import { fabric } from 'fabric';

const DrawingBook = () => {
    const leftCanvasRef = useRef(null);
    const rightCanvasRef = useRef(null);

    useEffect(() => {
        const leftCanvas = new fabric.Canvas(leftCanvasRef.current);
        const rightCanvas = new fabric.Canvas(rightCanvasRef.current);

        leftCanvas.isDrawingMode = true;
        rightCanvas.isDrawingMode = true;

        // Customize brush settings
        leftCanvas.freeDrawingBrush.color = "#000000";
        leftCanvas.freeDrawingBrush.width = 5;

        rightCanvas.freeDrawingBrush.color = "#000000";
        rightCanvas.freeDrawingBrush.width = 5;

        return () => {
            leftCanvas.dispose();
            rightCanvas.dispose();
        };
    }, []);

    const clearCanvases = () => {
        const leftCanvas = fabric.Canvas.getElement(leftCanvasRef.current);
        const rightCanvas = fabric.Canvas.getElement(rightCanvasRef.current);
        leftCanvas.clear();
        rightCanvas.clear();
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <h1 style={{ textAlign: 'center' }}>Draw in Your Book!</h1>
            <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '20px' }}>
                <div style={{ border: '2px solid #8B4513', marginRight: '5px', position: 'relative', overflow: 'hidden' }}>
                    <canvas ref={leftCanvasRef} width={300} height={400} style={{ border: '1px solid #ccc' }} />
                </div>
                <div style={{ border: '2px solid #8B4513', position: 'relative', overflow: 'hidden' }}>
                    <canvas ref={rightCanvasRef} width={300} height={400} style={{ border: '1px solid #ccc' }} />
                </div>
            </div>
            <button style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }} onClick={clearCanvases}>
                Clear Canvas
            </button>
        </div>
    );
};

export default DrawingBook;
