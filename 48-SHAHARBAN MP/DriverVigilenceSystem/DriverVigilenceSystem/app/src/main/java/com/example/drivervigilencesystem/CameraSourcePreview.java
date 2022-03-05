package com.example.drivervigilencesystem;

import android.content.Context;
import android.util.AttributeSet;
import android.util.Log;
import android.view.SurfaceHolder;
import android.view.SurfaceHolder.Callback;
import android.view.SurfaceView;
import android.view.ViewGroup;


import com.google.android.gms.common.images.Size;
import com.google.android.gms.vision.CameraSource;

import androidx.core.app.ActivityCompat;

import java.io.IOException;

public class CameraSourcePreview extends ViewGroup {
    private static final String TAG = "CameraSourcePreview";
    private CameraSource mCameraSource;
    private Context mContext;
    private GraphicOverlay mOverlay;
    private boolean mStartRequested = false;
    private boolean mSurfaceAvailable = false;
    private SurfaceView mSurfaceView;

    private class SurfaceCallback implements Callback {
        private SurfaceCallback() {
        }

        public void surfaceCreated(SurfaceHolder surface) {
            CameraSourcePreview.this.mSurfaceAvailable = true;
            try {
                CameraSourcePreview.this.startIfReady();
            } catch (IOException e) {
                Log.e(CameraSourcePreview.TAG, "Could not start camera source.", e);
            }
        }

        public void surfaceDestroyed(SurfaceHolder surface) {
            CameraSourcePreview.this.mSurfaceAvailable = false;
        }

        public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {
        }
    }

    public CameraSourcePreview(Context context, AttributeSet attrs) {
        super(context, attrs);
        this.mContext = context;
        this.mSurfaceView = new SurfaceView(context);
        this.mSurfaceView.getHolder().addCallback(new SurfaceCallback());
        addView(this.mSurfaceView);
    }

    public void start(CameraSource cameraSource) throws IOException {
        if (cameraSource == null) {
            stop();
        }
        this.mCameraSource = cameraSource;
        if (this.mCameraSource != null) {
            this.mStartRequested = true;
            startIfReady();
        }
    }

    public void start(CameraSource cameraSource, GraphicOverlay overlay) throws IOException {
        this.mOverlay = overlay;
        start(cameraSource);
    }

    public void stop() {
        if (this.mCameraSource != null) {
            this.mCameraSource.stop();
        }
    }

    public void release() {
        if (this.mCameraSource != null) {
            this.mCameraSource.release();
            this.mCameraSource = null;
        }
    }

    private void startIfReady() throws IOException {
        if (this.mStartRequested && this.mSurfaceAvailable && ActivityCompat.checkSelfPermission(this.mContext, "android.permission.CAMERA") == 0) {
            this.mCameraSource.start(this.mSurfaceView.getHolder());
            if (this.mOverlay != null) {
                Size size = this.mCameraSource.getPreviewSize();
                int min = Math.min(size.getWidth(), size.getHeight());
                int max = Math.max(size.getWidth(), size.getHeight());
                if (isPortraitMode()) {
                    this.mOverlay.setCameraInfo(min, max, this.mCameraSource.getCameraFacing());
                } else {
                    this.mOverlay.setCameraInfo(max, min, this.mCameraSource.getCameraFacing());
                }
                this.mOverlay.clear();
            }
            this.mStartRequested = false;
        }
    }

    protected void onLayout(boolean changed, int left, int top, int right, int bottom) {
        int width = driverhome.sScreenWidth;
        int height = driverhome.sScreenHeight;
        if (this.mCameraSource != null) {
            Size size = this.mCameraSource.getPreviewSize();
            if (size != null) {
                width = size.getWidth();
                height = size.getHeight();
            }
        }
        if (isPortraitMode()) {
            int tmp = width;
            width = height;
            height = tmp;
        }
        int layoutWidth = right - left;
        int layoutHeight = bottom - top;
        int childWidth = layoutWidth;
        int childHeight = (int) ((((float) layoutWidth) / ((float) width)) * ((float) height));
        if (childHeight > layoutHeight) {
            childHeight = layoutHeight;
            childWidth = (int) ((((float) layoutHeight) / ((float) height)) * ((float) width));
        }
        for (int i = 0; i < getChildCount(); i++) {
            getChildAt(i).layout(0, 0, childWidth, childHeight);
        }
        try {
            startIfReady();
        } catch (IOException e) {
            Log.e(TAG, "Could not start camera source.", e);
        }
    }

    private boolean isPortraitMode() {
        int orientation = this.mContext.getResources().getConfiguration().orientation;
        if (orientation == 2) {
            return false;
        }
        if (orientation == 1) {
            return true;
        }
        Log.d(TAG, "isPortraitMode returning false by default");
        return false;
    }
}
