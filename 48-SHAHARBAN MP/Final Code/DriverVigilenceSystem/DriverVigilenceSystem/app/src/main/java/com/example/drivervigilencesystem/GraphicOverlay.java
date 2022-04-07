package com.example.drivervigilencesystem;

import android.content.Context;
import android.graphics.Canvas;
import android.util.AttributeSet;
import android.view.View;

import java.util.HashSet;
import java.util.Set;

public class GraphicOverlay extends View {
    private int mFacing = 1;
    private Set<Graphic> mGraphics = new HashSet();
    private float mHeightScaleFactor = 1.0f;
    private final Object mLock = new Object();
    private int mPreviewHeight;
    private int mPreviewWidth;
    private float mWidthScaleFactor = 1.0f;

    public static abstract class Graphic {
        private GraphicOverlay mOverlay;

        public abstract void draw(Canvas canvas);

        public Graphic(GraphicOverlay overlay) {
            this.mOverlay = overlay;
        }

        public float scaleX(float horizontal) {
            return this.mOverlay.mWidthScaleFactor * horizontal;
        }

        public float scaleY(float vertical) {
            return this.mOverlay.mHeightScaleFactor * vertical;
        }

        public float translateX(float x) {
            if (this.mOverlay.mFacing == 1) {
                return ((float) this.mOverlay.getWidth()) - scaleX(x);
            }
            return scaleX(x);
        }

        public float translateY(float y) {
            return scaleY(y);
        }

        public void postInvalidate() {
            this.mOverlay.postInvalidate();
        }
    }

    public GraphicOverlay(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    public void clear() {
        synchronized (this.mLock) {
            this.mGraphics.clear();
        }
        postInvalidate();
    }

    public void add(Graphic graphic) {
        synchronized (this.mLock) {
            this.mGraphics.add(graphic);
        }
        postInvalidate();
    }

    public void remove(Graphic graphic) {
        synchronized (this.mLock) {
            this.mGraphics.remove(graphic);
        }
        postInvalidate();
    }

    public void setCameraInfo(int previewWidth, int previewHeight, int facing) {
        synchronized (this.mLock) {
            this.mPreviewWidth = previewWidth;
            this.mPreviewHeight = previewHeight;
            this.mFacing = facing;
        }
        postInvalidate();
    }

    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        synchronized (this.mLock) {
            if (!(this.mPreviewWidth == 0 || this.mPreviewHeight == 0)) {
                this.mWidthScaleFactor = ((float) canvas.getWidth()) / ((float) this.mPreviewWidth);
                this.mHeightScaleFactor = ((float) canvas.getHeight()) / ((float) this.mPreviewHeight);
            }
            for (Graphic graphic : this.mGraphics) {
                graphic.draw(canvas);
            }
        }
    }
}
