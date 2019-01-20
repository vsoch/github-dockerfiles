
The X server uses this directory to store the compiled version of the
current keymap and/or any scratch keymaps used by clients.  The X server
or some other tool might destroy or replace the files in this directory,
so it is not a safe place to store compiled keymaps for long periods of
time.  The default keymap for any server is usually stored in:
     X<num>-default.xkm
where <num> is the display number of the server in question, which makes
it possible for several servers *on the same host* to share the same 
directory.

Unless the X server is modified, sharing this directory between servers on
different hosts could cause problems.
                        X server test suite

This suite contains a set of tests to verify the behaviour of functions used
internally to the server.

= How it works =
Through some automake abuse, we link the test programs with the same static
libraries as the Xorg binary. The test suites can then call various functions
and verify their behaviour - without the need to start the server or connect
clients.

This testing only works for functions that do not rely on a particular state
of the X server. Unless the test suite replicates the expected state, which
may be difficult.

= How to run the tests =
Run "make check" in the test directory. This will compile the tests and execute
them in the order specified in the TESTS variable in test/Makefile.am.

Each set of tests related to a subsystem are available as a binary that can be
executed directly. For example, run "xkb" to perform some xkb-related tests.

== Adding a new test ==
When adding a new test, ensure that you add a short description of what the
test does and what the expected outcome is.

This is a submodule to access linux framebuffer devices.
It is supported to work as helper module (like vgahw)
for the chipset drivers.  There are functions for
saving/restoring/setting video modes, set palette entries,
and a few more helper functions.  Some of them can be
hooked directly into ScrnInfoRec.

In ../drivers/fbdev is a "chipset" driver.  It is a simple,
non-accelerated and hardware-independent driver which works
on top of this fbdevhw submodule.

  Gerd

--
Gerd Knorr <kraxel@goldbach.in-berlin.de>
		    Multi-monitor Mode Setting APIs
	           Keith Packard, <keithp@keithp.com
		   	   6 March 2007

1. Introduction

This document describes a set of mode setting APIs added in X server version
1.3 that support multiple monitors per card. These interfaces expose the
underlying hardware CRTC and output concepts to the xf86 DDX layer so that
the implementation of initial server setup and mode changes through
extensions can be shared across drivers. In addition, these new interfaces
support a new configuration mechanism as well which allows each monitor to
be customized separately providing a consistent cross-driver configuration
mechanism that supports the full range of output features.

All of the code implementing this interface can be found in hw/xfree86/modes
in the X server sources.

2. Overview

This document describes both the driver API and the configuration data
placed in xorg.conf; these are entirely separate as the driver has no
interaction with the configuration information at all. Much of the structure
here is cloned from the RandR extension version 1.2 additions which deal
with the same kinds of information.

2.1 API overview

The mode setting API is expressed through two new driver-visible objects,
the 'CRTC' (xf86CrtcRec) and the 'Output' (xf86OutputRec). A CRTC refers to
hardware within the video system that can scan a subset of the framebuffer
and generate a video signal. An Output receives that signal and transmits it
to a monitor, projector or other device.

The xf86CrtcRec and xf86OutputRec contain a small amount of state data
related to the object along with a pointer to a set of functions provided by
the driver that manipulate the object in fairly simple ways.

To emulate older behaviour, one of the outputs is picked as the 'compat'
output; this output changes over time as outputs are detected and used, the
goal is to always have one 'special' output which is used for operations
which need a single defined monitor (like XFree86-VidModeExtension mode
setting, RandR 1.1 mode setting, DDC property setting, etc.).

2.1.1 Output overview 

As outputs are connected to monitors, they hold a list of modes supported by
the monitor. If the monitor and output support DDC, then the list of modes
generally comes from the EDID data in the monitor. Otherwise, the server
uses the standard VESA modes, pruned by monitor timing. If the configuration
file doesn't contain monitor timing data, the server uses default timing
information which supports 640x480, 800x600 and 1024x768 all with a 60Hz
refresh rate.

As hardware often limits possible configuration combinations, each output
knows the set of CRTCs that it can be connected to as well as the set of
other outputs which can be simutaneously connected to a CRTC.

2.1.2 CRTC overview

CRTCs serve only to stream frame buffer data to outputs using a mode line.
Ideally, they would not be presented to the user at all, and in fact the
configuration file doesn't expose them. The RandR 1.2 protocol does, but the
hope there is that client-side applications will hide them carefully away.

Each crtc has an associated cursor, along with the current configuration.
All of the data needed to determine valid configurations is contained within
the Outputs.

2.2 Configuration overview

As outputs drive monitors, the "Monitor" section has been repurposed to
define their configuration. This provides for a bit more syntax than
the large list of driver-specific options that were used in the past for
similar configuration.

However, the existing "Monitor" section referenced by the active "Screen"
section no longer has any use at all; some sensible meaning for this
parameter is needed now that a Screen can have multiple Monitors.

3. Public Functions

3.1 PreInit functions

These functions should be used during the driver PreInit phase, they are
arranged in the order they should be invoked.

    void
    xf86CrtcConfigInit (ScrnInfoPtr			scrn
			const xf86CrtcConfigFuncsRec	*funcs)

This function allocates and initializes structures needed to track CRTC and
Output state.

    void
    xf86CrtcSetSizeRange (ScrnInfoPtr scrn,
			  int minWidth, int minHeight,
			  int maxWidth, int maxHeight)

This sets the range of screen sizes supported by the driver.

    xf86CrtcPtr
    xf86CrtcCreate (ScrnInfoPtr             scrn,
		    const xf86CrtcFuncsRec  *funcs)
    
Create one CRTC object. See the discussion below for a description of the
contents of the xf86CrtcFuncsRec. Note that this is done in PreInit, so it
should not be re-invoked at each server generation. Create one of these for
each CRTC present in the hardware.
    
    xf86OutputPtr
    xf86OutputCreate (ScrnInfoPtr              scrn,
		      const xf86OutputFuncsRec *funcs,
		      const char	       *name)

Create one Output object. See the discussion below for a description of the
contents of the xf86OutputFuncsRec. This is also called from PreInit and
need not be re-invoked at each ScreenInit time. An Output should be created
for every Output present in the hardware, not just for outputs which have
detected monitors.
    
    Bool
    xf86OutputRename (xf86OutputPtr output, const char *name)

If necessary, the name of an output can be changed after it is created using
this function.
    
    Bool
    xf86InitialConfiguration (ScrnInfoPtr scrn, Bool canGrow)

Using the resources provided, and the configuration specified by the user,
this function computes an initial configuration for the server. It tries to
enable as much hardware as possible using some fairly simple heuristics. 

The 'canGrow' parameter indicates that the frame buffer does not have a fixed
size. When the frame buffer has a fixed size, the configuration selects a
'reasonablely large' frame buffer so that common reconfiguration options are
possible. For resizable frame buffers, the frame buffer is set to the smallest
size that encloses the desired configuration.
    
3.2 ScreenInit functions

These functions should be used during the driver ScreenInit phase.

    Bool
    xf86DiDGAInit (ScreenPtr screen, unsigned long dga_address)

This function provides driver-independent accelerated DGA support for some
of the DGA operations; using this, the driver can avoid needing to implement
any of the rest of DGA.

    Bool
    xf86SaveScreen(ScreenPtr pScreen, int mode)

Stick this in pScreen->SaveScreen and the core X screen saver will be
implemented by disabling outputs and crtcs using their dpms functions.

    void
    xf86DPMSSet(ScrnInfoPtr scrn, int mode, int flags)

Pass this function to xf86DPMSInit and all DPMS mode switching will be
managed by using the dpms functions provided by the Outputs and CRTCs.

    Bool
    xf86CrtcScreenInit (ScreenPtr screen)

This function completes the screen initialization process for the crtc and
output objects. Call it near the end of the ScreenInit function, after the
frame buffer and acceleration layers have been added.

3.3 EnterVT functions

Functions used during EnterVT, or whenever the current configuration needs
to be applied to the hardware.

    Bool
    xf86SetDesiredModes (ScrnInfoPtr scrn)

xf86InitialConfiguration selects the desired configuration at PreInit time;
when the server finally hits ScreenInit, xf86SetDesiredModes is used by the
driver to take that configuration and apply it to the hardware. In addition,
successful mode selection at other times updates the configuration that will
be used by this function, so LeaveVT/EnterVT pairs can simply invoke this
and return to the previous configuration.

3.4 SwitchMode functions

Functions called from the pScrn->SwitchMode hook, which is used by the
XFree86-VidModeExtension and the keypad mode switch commands.

    Bool
    xf86SetSingleMode (ScrnInfoPtr	scrn, 
		       DisplayModePtr   desired,
		       Rotation		rotation)

This function applies the specified mode to all active outputs. Which is to
say, it picks reasonable modes for all active outputs, attempting to get the
screen to the specified size while not breaking anything that is currently
working.

3.7 get_modes functions

Functions called during output->get_modes to help build lists of modes

    xf86MonPtr
    xf86OutputGetEDID (xf86OutputPtr output, I2CBusPtr pDDCBus)

This returns the EDID data structure for the 'output' using the I2C bus
'pDDCBus'. This has no effect on 'output' itself.

    void
    xf86OutputSetEDID (xf86OutputPtr output, xf86MonPtr edid_mon)

Once the EDID data has been fetched, this call applies the EDID data to the
output object, setting the physical size and also various properties, like
the DDC root window property (when output is the 'compat' output), and the
RandR 1.2 EDID output properties.

    DisplayModePtr
    xf86OutputGetEDIDModes (xf86OutputPtr output)

Given an EDID data structure, this function computes a list of suitable
modes. This function also applies a sequence of 'quirks' during this process
so that the returned modes may not actually match the mode data present in
the EDID data.

3.6 Other functions

These remaining functions in the API can be used by the driver as needed.

    Bool
    xf86CrtcSetMode (xf86CrtcPtr crtc, DisplayModePtr mode, Rotation rotation,
		     int x, int y)

Applies a mode to a CRTC. All of the outputs which are currently using the
specified CRTC are included in the mode setting process. 'x' and 'y' are the
offset within the frame buffer that the crtc is placed at. No checking is
done in this function to ensure that the mode is usable by the active
outputs.
    
    void
    xf86ProbeOutputModes (ScrnInfoPtr pScrn, int maxX, int maxY)

This discards the mode lists for all outputs, re-detects monitor presence
and then acquires new mode lists for all monitors which are not disconnected.
Monitor configuration data is used to modify the mode lists returned by the
outputs. 'maxX' and 'maxY' limit the maximum size modes that will be
returned.
    
    void
    xf86SetScrnInfoModes (ScrnInfoPtr pScrn)

This copies the 'compat' output mode list into the pScrn modes list which is
used by the XFree86-VidModeExtension and the keypad mode switching
operations. The current 'desired' mode for the CRTC associated with the
'compat' output is placed first in this list to indicate the current mode.
Usually, the driver won't need to call this function as
xf86InitialConfiguration will do so automatically, as well as any RandR
functions which reprobe for modes. However, if the driver reprobes for modes
at other times using xf86ProbeOutputModes, this function needs to be called.
    
    Bool
    xf86DiDGAReInit (ScreenPtr pScreen)

This is similar to xf86SetScrnInfoModes, but it applies the 'compat' output
mode list to the set of modes advertised by the DGA extension; it needs to
be called whenever xf86ProbeOutputModes is invoked.

    void
    xf86DisableUnusedFunctions(ScrnInfoPtr pScrn)

After any sequence of calls using xf86CrtcSetMode, this function cleans up
any leftover Output and CRTC objects by disabling them, saving power. It is
safe to call this whenever the server is running as it only disables objects
which are not currently in use.
    
4. CRTC operations

4.1 CRTC functions

These functions provide an abstract interface for the CRTC object; most
manipulation of the CRTC object is done through these functions.

    void
    crtc->funcs->dpms (xf86CrtcPtr crtc, int mode)

Where 'mode' is one of DPMSModeOff, DPMSModeSuspend, DPMSModeStandby or
DPMSModeOn. This requests that the crtc go to the specified power state.
When changing power states, the output dpms functions are invoked before the
crtc dpms functions.

    void
    crtc->funcs->save (xf86CrtcPtr crtc)
	
    void
    crtc->funcs->restore (xf86CrtcPtr crtc)

Preserve/restore any register contents related to the CRTC. These are
strictly a convenience for the driver writer; if the existing driver has
fully operation save/restore functions, you need not place any additional
code here. In particular, the server itself never uses this function.

    Bool
    crtc->funcs->lock (xf86CrtcPtr crtc)
	
    void
    crtc->funcs->unlock (xf86CrtcPtr crtc)

These functions are invoked around mode setting operations; the intent is
that DRI locking be done here to prevent DRI applications from manipulating
the hardware while the server is busy changing the output configuration. If
the lock function returns FALSE, the unlock function will not be invoked.

    Bool
    crtc->funcs->mode_fixup (xf86CrtcPtr crtc, 
			     DisplayModePtr mode,
			     DisplayModePtr adjusted_mode)

This call gives the CRTC a chance to see what mode will be set and to
comment on the mode by changing 'adjusted_mode' as needed. This function
shall not modify the state of the crtc hardware at all. If the CRTC cannot
accept this mode, this function may return FALSE.

    void
    crtc->funcs->prepare (xf86CrtcPtr crtc)

This call is made just before the mode is set to make the hardware ready for
the operation. A usual function to perform here is to disable the crtc so
that mode setting can occur with clocks turned off and outputs deactivated.

    void
    crtc->funcs->mode_set (xf86CrtcPtr crtc,
			   DisplayModePtr mode,
			   DisplayModePtr adjusted_mode)

This function applies the specified mode (possibly adjusted by the CRTC
and/or Outputs).

    void
    crtc->funcs->commit (xf86CrtcPtr crtc)

Once the mode has been applied to the CRTC and Outputs, this function is
invoked to let the hardware turn things back on.

    void
    crtc->funcs->gamma_set (xf86CrtcPtr crtc, CARD16 *red,
			    CARD16 *green, CARD16 *blue, int size)

This function adjusts the gamma ramps for the specified crtc.

    void *
    crtc->funcs->shadow_allocate (xf86CrtcPtr crtc, int width, int height)

This function allocates frame buffer space for a shadow frame buffer. When
allocated, the crtc must scan from the shadow instead of the main frame
buffer. This is used for rotation. The address returned is passed to the
shadow_create function. This function should return NULL on failure.

    PixmapPtr
    crtc->funcs->shadow_create (xf86CrtcPtr crtc, void *data,
				int width, int height)

This function creates a pixmap object that will be used as a shadow of the
main frame buffer for CRTCs which are rotated or reflected. 'data' is the
value returned by shadow_allocate.

    void
    crtc->funcs->shadow_destroy (xf86CrtcPtr crtc, PixmapPtr pPixmap,
				 void *data)

Destroys any associated shadow objects. If pPixmap is NULL, then a pixmap
was not created, but 'data' may still be non-NULL indicating that the shadow
had been allocated.

    void
    crtc->funcs->destroy (xf86CrtcPtr crtc)

When a CRTC is destroyed (which only happens in error cases), this function
can clean up any driver-specific data.

4.2 CRTC fields

The CRTC object is not opaque; there are several fields of interest to the
driver writer.

    struct _xf86Crtc {
	/**
	 * Associated ScrnInfo
	 */
	ScrnInfoPtr     scrn;
    
	/**
	 * Active state of this CRTC
	 *
	 * Set when this CRTC is driving one or more outputs
	 */
	Bool            enabled;
    
	/** Track whether cursor is within CRTC range  */
	Bool            cursorInRange;
    
	/** Track state of cursor associated with this CRTC */
	Bool            cursorShown;
    
	/**
	 * Active mode
	 *
	 * This reflects the mode as set in the CRTC currently
	 * It will be cleared when the VT is not active or
	 * during server startup
	 */
	DisplayModeRec  mode;
	Rotation        rotation;
	PixmapPtr       rotatedPixmap;
	void            *rotatedData;
    
	/**
	 * Position on screen
	 *
	 * Locates this CRTC within the frame buffer
	 */
	int             x, y;
    
	/**
	 * Desired mode
	 *
	 * This is set to the requested mode, independent of
	 * whether the VT is active. In particular, it receives
	 * the startup configured mode and saves the active mode
	 * on VT switch.
	 */
	DisplayModeRec  desiredMode;
	Rotation        desiredRotation;
	int             desiredX, desiredY;
    
	/** crtc-specific functions */
	const xf86CrtcFuncsRec *funcs;
    
	/**
	 * Driver private
	 *
	 * Holds driver-private information
	 */
	void            *driver_private;
    #ifdef RANDR_12_INTERFACE
	/**
	 * RandR crtc
	 *
	 * When RandR 1.2 is available, this
	 * points at the associated crtc object
	 */
	RRCrtcPtr       randr_crtc;
    #else
	void            *randr_crtc;
    #endif
    };

    
5. Output functions.

6. Configuration

Because the configuration file syntax is fixed,
this was done by creating new "Driver" section options that hook specific
outputs to specific "Monitor" sections in the file. The option:
section of the form:

	Option	"monitor-VGA" "My VGA Monitor"

connects the VGA output of this driver to the "Monitor" section with
Identifier "My VGA Monitor". All of the usual monitor options can now be
placed in that "Monitor" section and will be applied to the VGA output
configuration.
Xephyr README
=============


What Is It ?
============

Xephyr is a a kdrive server that outputs to a window on a pre-existing
'host' X display. Think Xnest but with support for modern extensions
like composite, damage and randr. 

Unlike Xnest which is an X proxy, i.e.  limited to the
capabilities of the host X server, Xephyr is a real X server which
uses the host X server window as "framebuffer" via fast SHM XImages.

It also has support for 'visually' debugging what the server is
painting.


How To Use 
==========

You probably want to run like;

Xephyr :1 -ac -screen 800x600 &

Then set DISPLAY=:1 and run whatever X apps you like.

Use 'xrandr' to change to orientation/size. 

There is a '-parent' switch which works just like Xnests ( for use
with things like matchbox-nest - http://matchbox.handhelds.org ).

There is also a '-host-cursor' switch to set 'cursor acceleration' -
The host's cursor is reused. This is only really there to aid
debugging by avoiding server paints for the cursor. Performance
improvement is negiable. 

Send a SIGUSR1 to the server ( eg kill -USR1 `pidof Xephyr` ) to
toggle the debugging mode. In this mode red rectangles are painted to
screen areas getting painted before painting the actual content. The
delay between this can be altered by setting a XEPHYR_PAUSE env var to
a value in micro seconds.


Caveats
=======

 - Depth is limited to being the same as the host. 
   *Update* As of 8/11/2004. Xephyr can now do 8bpp & 16bpp 
            on 24bpp host.

 - Rotated displays are currently updated via full blits. This
   is slower than a normal oprientated display. Debug mode will
   therefor not be of much use rotated.  

 - The '-host-cursor' cursor is static in its appearence. 

 - The build gets a warning about 'nanosleep'. I think the various '-D'
   build flags are causing this. I havn't figured as yet how to work
   round it. It doesn't appear to break anything however. 

 - Keyboard handling is basic but works. 

 - Mouse button 5 probably wont work. 





Matthew Allum <mallum@o-hand.com> 2004 


                            Generic Rootless Layer
                                 Version 1.0
                                July 13, 2004

                               Torrey T. Lyons
                              torrey@xfree86.org


Introduction

        The generic rootless layer allows an X server to be implemented 
on top of another window server in a cooperative manner. This allows the 
X11 windows and native windows of the underlying window server to 
coexist on the same screen. The layer is called "rootless" because the root 
window of the X server is generally not drawn. Instead, each top-level 
child of the root window is represented as a separate on-screen window by 
the underlying window server. The layer is referred to as "generic" 
because it abstracts away the details of the underlying window system and 
contains code that is useful for any rootless X server. The code for the 
generic rootless layer is located in xc/programs/Xserver/miext/rootless. To 
build a complete rootless X server requires a specific rootless 
implementation, which provides functions that allow the generic rootless 
layer to interact with the underlying window system.


Concepts

        In the context of a rootless X server the term window is used to 
mean many fundamentally different things. For X11 a window is a DDX 
resource that describes a visible, or potentially visible, rectangle on the 
screen. A top-level window is a direct child of the root window. To avoid 
confusion, an on-screen native window of the underlying window system 
is referred to as a "frame". The generic rootless layer associates each 
mapped top-level X11 window with a frame. An X11 window may be said 
to be "framed" if it or its top-level parent is represented by a frame.

        The generic rootless layer models each frame as being backed at 
all times by a backing buffer, which is periodically flushed to the screen. 
If the underlying window system does not provide a backing buffer for 
frames, this must be done by the rootless implementation. The generic 
rootless layer model does not assume it always has access to the frames' 
backing buffers. Any drawing to the buffer will be proceeded by a call to 
the rootless implementation's StartDrawing() function and StopDrawing() 
will be called when the drawing is concluded. The address of the frame's 
backing buffer is returned by the StartDrawing() function and it can 
change between successive calls.

        Because each frame is assumed to have a backing buffer, the 
generic rootless layer will stop Expose events being generated when the 
regions of visibility of a frame change on screen. This is similar to backing 
store, but backing buffers are different in that they always store a copy of 
the entire window contents, not just the obscured portions. The price paid 
in increased memory consumption is made up by the greatly decreased 
complexity in not having to track and record regions as they are obscured.


Rootless Implementation

        The specifics of the underlying window system are provided to the 
generic rootless layer through rootless implementation functions, compile-
time options, and runtime parameters. The rootless implementation 
functions are a list of functions that allow the generic rootless layer to 
perform operations such as creating, destroying, moving, and resizing 
frames. Some of the implementation functions are optional. A detailed 
description of the rootless implementation functions is provided in 
Appendix A.

        By design, a rootless implementation should only have to include 
the rootless.h header file. The rootlessCommon.h file contains definitions 
internal to the generic rootless layer. (If you find you need to use 
rootlessCommon.h in your implementation, let the generic rootless layer 
maintainers know. This could be an area where the generic rootless layer 
should be generalized.) A rootless implementation should also modify 
rootlessConfig.h to specify compile time options for its platform.

        The following compile-time options are defined in 
rootlessConfig.h:

      o ROOTLESS_PROTECT_ALPHA: By default for a color bit depth of 24 and
        32 bits per pixel, fb will overwrite the "unused" 8 bits to optimize
        drawing speed. If this is true, the alpha channel of frames is
        protected and is not modified when drawing to them. The bits 
        containing the alpha channel are defined by the macro 
        RootlessAlphaMask(bpp), which should return a bit mask for 
        various bits per pixel.

      o ROOTLESS_REDISPLAY_DELAY: Time in milliseconds between updates to
        the underlying window server. Most operations will be buffered until
        this time has expired.

      o ROOTLESS_RESIZE_GRAVITY: If the underlying window system supports it,
        some frame resizes can be optimized by relying on the frame contents
        maintaining a particular gravity during the resize. In this way less
        of the frame contents need to be preserved by the generic rootless
        layer. If true, the generic rootless layer will pass gravity hints
        during resizing and rely on the frame contents being preserved
        accordingly.

        The following runtime options are defined in rootless.h:

      o rootlessGlobalOffsetX, rootlessGlobalOffsetY: These specify the global
        offset that is applied to all screens when converting from
        screen-local to global coordinates.

      o rootless_CopyBytes_threshold, rootless_CopyWindow_threshold:
        The minimum number of bytes or pixels for which to use the rootless
        implementation's respective acceleration function. The rootless
        acceleration functions are all optional so these will only be used
        if the respective acceleration function pointer is not NULL.


Accelerated Drawing

	The rootless implementation typically does not have direct access 
to the hardware. Its access to the graphics hardware is generally through 
the API of the underlying window system. This underlying API may not 
overlap well with the X11 drawing primitives. The generic rootless layer 
falls back to using fb for all its 2-D drawing. Providing optional rootless 
implementation acceleration functions can accelerate some graphics 
primitives and some window functions. Typically calling through to the 
underlying window systems API will not speed up these operations for 
small enough areas. The rootless_*_threshold runtime options allow the 
rootless implementation to provide hints for when the acceleration 
functions should be used instead of fb.


Alpha Channel Protection

	If the bits per pixel is greater then the color bit depth, the contents 
of the extra bits are undefined by the X11 protocol. Some window systems 
will use these extra bits as an alpha channel. The generic rootless layer can 
be configured to protect these bits and make sure they are not modified by 
other parts of the X server. To protect the alpha channel 
ROOTLESS_PROTECT_ALPHA and RootlessAlphaMask(bpp) must be 
set appropriately as described under the compile time options. This 
ensures that the X11 graphics primitives do not overwrite the alpha 
channel in an attempt to optimize drawing. In addition, the window 
functions PaintWindow() and Composite() must be replaced by alpha 
channel safe variants. These are provided in rootless/safeAlpha.


Credits

	The generic rootless layer was originally conceived and developed 
by Greg Parker as part of the XDarwin X server on Mac OS X. John 
Harper made later optimizations to this code but removed its generic 
independence of the underlying window system. Torrey T. Lyons 
reintroduced the generic abstractions and made the rootless code suitable 
for use by other X servers.


Appendix A: Rootless Implementation Functions

	The rootless implementation functions are defined in rootless.h. It 
is intended that rootless.h contains the complete interface that is needed by 
rootless implementations. The definitions contained in rootlessCommon.h 
are intended for internal use by the generic rootless layer and are more 
likely to change.

	Most of these functions take a RootlessFrameID as a parameter. 
The RootlessFrameID is an opaque object that is returned by the 
implementation's CreateFrame() function. The generic rootless layer does 
not use this frame id other than to pass it back to the rootless 
implementation to indicate the frame to operate on.

/*
 * Create a new frame.
 *  The frame is created unmapped.
 *
 *  pFrame      RootlessWindowPtr for this frame should be completely
 *              initialized before calling except for pFrame->wid, which
 *              is set by this function.
 *  pScreen     Screen on which to place the new frame
 *  newX, newY  Position of the frame.
 *  pNewShape   Shape for the frame (in frame-local coordinates). NULL for
 *              unshaped frames.
 */
typedef Bool (*RootlessCreateFrameProc)
    (RootlessWindowPtr pFrame, ScreenPtr pScreen, int newX, int newY,
     RegionPtr pNewShape);

/*
 * Destroy a frame.
 *  Drawing is stopped and all updates are flushed before this is called.
 *
 *  wid         Frame id
 */
typedef void (*RootlessDestroyFrameProc)
    (RootlessFrameID wid);

/*
 * Move a frame on screen.
 *  Drawing is stopped and all updates are flushed before this is called.
 *
 *  wid         Frame id
 *  pScreen     Screen to move the new frame to
 *  newX, newY  New position of the frame
 */
typedef void (*RootlessMoveFrameProc) 
    (RootlessFrameID wid, ScreenPtr pScreen, int newX, int newY);

/*
 * Resize and move a frame.
 *  Drawing is stopped and all updates are flushed before this is called.
 *
 *  wid         Frame id
 *  pScreen     Screen to move the new frame to
 *  newX, newY  New position of the frame
 *  newW, newH  New size of the frame
 *  gravity     Gravity for window contents (rl_gravity_enum). This is always
 *              RL_GRAVITY_NONE unless ROOTLESS_RESIZE_GRAVITY is set.
 */
typedef void (*RootlessResizeFrameProc)
    (RootlessFrameID wid, ScreenPtr pScreen,
     int newX, int newY, unsigned int newW, unsigned int newH,
     unsigned int gravity);

/*
 * Change frame ordering (AKA stacking, layering).
 *  Drawing is stopped before this is called. Unmapped frames are mapped by
 *  setting their ordering.
 *
 *  wid         Frame id
 *  nextWid     Frame id of frame that is now above this one or NULL if this
 *              frame is at the top.
 */
typedef void (*RootlessRestackFrameProc)
    (RootlessFrameID wid, RootlessFrameID nextWid);

/*
 * Change frame's shape.
 *  Drawing is stopped before this is called.
 *
 *  wid         Frame id
 *  pNewShape   New shape for the frame (in frame-local coordinates)
 *              or NULL if now unshaped.
 */
typedef void (*RootlessReshapeFrameProc)
    (RootlessFrameID wid, RegionPtr pNewShape);

/*
 * Unmap a frame.
 *
 *  wid         Frame id
 */
typedef void (*RootlessUnmapFrameProc)
    (RootlessFrameID wid);

/*
 * Start drawing to a frame.
 *  Prepare a frame for direct access to its backing buffer.
 *
 *  wid         Frame id
 *  pixelData   Address of the backing buffer (returned)
 *  bytesPerRow Width in bytes of the backing buffer (returned)
 */
typedef void (*RootlessStartDrawingProc)
    (RootlessFrameID wid, char **pixelData, int *bytesPerRow);

/*
 * Stop drawing to a frame.
 *  No drawing to the frame's backing buffer will occur until drawing
 *  is started again.
 *
 *  wid         Frame id
 *  flush       Flush drawing updates for this frame to the screen.
 */
typedef void (*RootlessStopDrawingProc)
    (RootlessFrameID wid, Bool flush);

/*
 * Flush drawing updates to the screen.
 *  Drawing is stopped before this is called.
 *
 *  wid         Frame id
 *  pDamage     Region containing all the changed pixels in frame-local
 *              coordinates. This is clipped to the window's clip.
 */
typedef void (*RootlessUpdateRegionProc)
    (RootlessFrameID wid, RegionPtr pDamage);

/*
 * Mark damaged rectangles as requiring redisplay to screen.
 *
 *  wid         Frame id
 *  nrects      Number of damaged rectangles
 *  rects       Array of damaged rectangles in frame-local coordinates
 *  shift_x,    Vector to shift rectangles by
 *   shift_y
 */
typedef void (*RootlessDamageRectsProc)
    (RootlessFrameID wid, int nrects, const BoxRec *rects,
     int shift_x, int shift_y);

/*
 * Switch the window associated with a frame. (Optional)
 *  When a framed window is reparented, the frame is resized and set to
 *  use the new top-level parent. If defined this function will be called
 *  afterwards for implementation specific bookkeeping.
 *
 *  pFrame      Frame whose window has switched
 *  oldWin      Previous window wrapped by this frame
 */
typedef void (*RootlessSwitchWindowProc)
    (RootlessWindowPtr pFrame, WindowPtr oldWin);

/*
 * Copy bytes. (Optional)
 *  Source and destinate may overlap and the right thing should happen.
 *
 *  width       Bytes to copy per row
 *  height      Number of rows
 *  src         Source data
 *  srcRowBytes Width of source in bytes
 *  dst         Destination data
 *  dstRowBytes Width of destination in bytes
 */
typedef void (*RootlessCopyBytesProc)
    (unsigned int width, unsigned int height,
     const void *src, unsigned int srcRowBytes,
     void *dst, unsigned int dstRowBytes);

/*
 * Copy area in frame to another part of frame. (Optional)
 *
 *  wid         Frame id
 *  dstNrects   Number of rectangles to copy
 *  dstRects    Array of rectangles to copy
 *  dx, dy      Number of pixels away to copy area
 */
typedef void (*RootlessCopyWindowProc)
    (RootlessFrameID wid, int dstNrects, const BoxRec *dstRects,
     int dx, int dy);

