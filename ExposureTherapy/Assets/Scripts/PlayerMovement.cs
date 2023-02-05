using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    [Header("Movement")]
    public float moveSpeed;

    public float groundDrag;

    [Header("Ground Check")]
    public float playerHeight;
    public LayerMask whatIsGround;
    bool grounded;

    public Transform orientation;

    float horizontalInput;
    float verticalInput;

    bool isDisabled;

    Vector3 moveDirection;

    Rigidbody rb;
    AudioSource footsteps;

    bool walking;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        footsteps = GetComponent<AudioSource>();
        rb.freezeRotation = true;
        isDisabled = false;
        walking = false;
    }

    // Update is called once per frame
    void Update()
    {
        grounded = Physics.Raycast(transform.position, Vector3.down, playerHeight * 0.5f + 0.2f, whatIsGround);

        if (!isDisabled)
        {
            MyInput();
        }
        SpeedControl();

        if (grounded)
        {
            rb.drag = groundDrag;
        }
        else
        {
            rb.drag = 0;
        }
    }

    private void FixedUpdate()
    {
        MovePlayer();
    }

    private void MyInput()
    {
        horizontalInput = Input.GetAxisRaw("Horizontal");
        verticalInput = Input.GetAxisRaw("Vertical");
        if ((horizontalInput != 0 || verticalInput != 0) && !walking)
        {
            print("Started walking");
            walking = true;
            footsteps.Play();
        }
        else if ((horizontalInput == 0 && verticalInput == 0) && walking)
        {
            print("Stopped walking");
            walking = false;
            footsteps.Stop();
        }
    }

    private void MovePlayer()
    {
        moveDirection = orientation.forward * verticalInput + orientation.right * horizontalInput;

        rb.AddForce(moveDirection.normalized * moveSpeed * 10f, ForceMode.Force);
    }

    private void SpeedControl()
    {
        Vector3 flatVel = new Vector3(rb.velocity.x, 0f, rb.velocity.z);

        if (flatVel.magnitude > moveSpeed)
        {
            Vector3 limitedVel = flatVel.normalized * moveSpeed;
            rb.velocity = new Vector3(limitedVel.x, rb.velocity.y, limitedVel.z);
        }
    }

    public void DisableMovement()
    {
        isDisabled = true;
    }
}
