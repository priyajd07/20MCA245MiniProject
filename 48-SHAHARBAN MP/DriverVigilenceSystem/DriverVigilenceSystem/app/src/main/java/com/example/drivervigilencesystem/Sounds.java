package com.example.drivervigilencesystem;

import android.annotation.TargetApi;
import android.app.Activity;
import android.media.AudioAttributes;
import android.media.AudioManager;
import android.media.SoundPool;
import android.media.SoundPool.Builder;
import android.media.SoundPool.OnLoadCompleteListener;
import android.os.Build.VERSION;

public class Sounds {
    private static final int MAX_STREAMS = 1;
    private static float sActVolume;
    private static boolean sLoaded = false;
    private static float sMaxVolume;
    private static int sSoundID;
    private static SoundPool sSoundPool;
    private static float sVolume;

    public static void initAlertSound(Activity activity) {
        AudioManager audioManager = (AudioManager) activity.getSystemService("audio");
        sActVolume = (float) audioManager.getStreamVolume(3);
        sMaxVolume = (float) audioManager.getStreamMaxVolume(3);
        sVolume = sActVolume / sMaxVolume;
        activity.setVolumeControlStream(3);
        if (VERSION.SDK_INT >= 21) {
            createSoundPoolWithBuilder();
        } else {
            createSoundPoolWithConstructor();
        }
        sSoundPool.setOnLoadCompleteListener(new OnLoadCompleteListener() {
            public void onLoadComplete(SoundPool soundPool, int sampleId, int status) {
                Sounds.sLoaded = true;
            }
        });
        sSoundID = sSoundPool.load(activity, R.raw.beep, MAX_STREAMS);
    }

    @TargetApi(21)
    private static void createSoundPoolWithBuilder() {
        sSoundPool = new Builder().setAudioAttributes(new AudioAttributes.Builder().setUsage(4).setContentType(4).build()).setMaxStreams(MAX_STREAMS).build();
    }

    private static void createSoundPoolWithConstructor() {
        sSoundPool = new SoundPool(MAX_STREAMS, 3, 0);
    }

    public static void alert() {
        if (sLoaded) {
            sSoundPool.play(sSoundID, sVolume, sVolume, MAX_STREAMS, 0, 1.0f);
        }
    }

    public static void changeState(boolean isMute) {
        if (isMute) {
            sVolume = 0.0f;
        } else {
            sVolume = sActVolume / sMaxVolume;
        }
    }
}
